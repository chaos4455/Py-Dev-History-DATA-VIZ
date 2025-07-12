import os
import hashlib
from datetime import datetime
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import warnings

# --- Configurações Iniciais ---
warnings.simplefilter(action='ignore', category=FutureWarning)

# Diretório padrão para análise
DEFAULT_DIR = r"c:\seu-diretorio-de-projetos-aqui" 
# Diretório para salvar os gráficos e o relatório
OUTPUT_DIR = "analise_codigo_output"

# --- Estilização dos Gráficos (Inspirado no exemplo de vendas) ---
DARK_BG_COLOR = '#1f1f1f'
GRID_COLOR = '#555555'
TEXT_COLOR = '#dddddd'
plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = DARK_BG_COLOR
plt.rcParams['axes.facecolor'] = DARK_BG_COLOR
plt.rcParams['axes.labelcolor'] = TEXT_COLOR
plt.rcParams['xtick.color'] = TEXT_COLOR
plt.rcParams['ytick.color'] = TEXT_COLOR
plt.rcParams['axes.edgecolor'] = GRID_COLOR
plt.rcParams['grid.color'] = GRID_COLOR
plt.rcParams['legend.facecolor'] = DARK_BG_COLOR
plt.rcParams['legend.edgecolor'] = GRID_COLOR
plt.rcParams['legend.labelcolor'] = TEXT_COLOR
plt.rcParams['axes.titlecolor'] = TEXT_COLOR

# --- Listas de Pastas a Ignorar (Consolidado dos exemplos) ---
PASTAS_IGNORADAS = set([
    'venv', '.venv', 'env', '.env', 'lib', 'lib64', 'site-packages', 'dist-packages', 'eggs',
    'pip-wheel-metadata', '__pycache__', 'build', 'dist', 'docs', 'doc', 'etc', 'static',
    'templates', 'media', 'node_modules', '.git', '.svn', '.hg', '.CVS', '.idea', '.vscode',
    '.spyder-py3', '.pylint.d', '.mypy_cache', '.pytest_cache', '__pypackages__', 'wheelhouse',
    'htmlcov', '.coverage', 'coverage.xml', '*.egg-info', 'MANIFEST', 'sphinx-build', '_build',
    '_static', '_templates', 'data', 'resources', 'assets', 'out', 'output', 'target', 'log',
    'logs', 'tmp', 'temp', 'cache', 'caches', '.gradle', '.mvn', '.docker', '.vagrant', '.terraform',
    '.ansible', '.terraform.lock.hcl', '.DS_Store', '.Trashes', '$RECYCLE.BIN', 'System Volume Information',
    '._*', '._.Trashes', '._.DS_Store', '.localized', '.AppleDouble', 'analise_codigo_output' # Ignora a própria pasta de output
])
PASTAS_PARA_MANTER = {'test', 'tests', 'testing', 'integration-tests', 'unit-tests', 'functional-tests', 'benchmark', 'benchmarks', 'example', 'examples', 'sample', 'samples', 'notebooks'}
PASTAS_IGNORADAS = PASTAS_IGNORADAS.difference(PASTAS_PARA_MANTER)


class AnalisadorDeCodigo:
    """
    Classe para varrer, analisar e preparar dados de arquivos Python.
    """
    def __init__(self, diretorio_base):
        if not os.path.isdir(diretorio_base):
            raise ValueError(f"O diretório fornecido não existe: {diretorio_base}")
        self.diretorio_base = diretorio_base
        self.dados_arquivos = []
        self.df = None

    def varrer_arquivos(self):
        """
        Varre o diretório recursivamente, coletando metadados de arquivos .py
        e lidando com duplicatas baseadas no hash MD5 (mantém o mais antigo).
        """
        print(f"Iniciando varredura em '{self.diretorio_base}'...")
        arquivos_processados_md5 = {}  # {md5_hash: {mod_time: timestamp, dados: {}}}

        for pasta_raiz, subpastas, arquivos in os.walk(self.diretorio_base, topdown=True):
            subpastas[:] = [
                d for d in subpastas if d.lower() not in PASTAS_IGNORADAS and not d.startswith('.')
            ]
            for arquivo in arquivos:
                if not arquivo.endswith(".py"):
                    continue

                caminho_completo = os.path.join(pasta_raiz, arquivo)
                try:
                    tamanho_kb = os.path.getsize(caminho_completo) / 1024
                    if tamanho_kb == 0:
                        continue
                    
                    with open(caminho_completo, 'rb') as f:
                        conteudo_bytes = f.read()

                    mod_timestamp = os.path.getmtime(caminho_completo)
                    md5_hash = hashlib.md5(conteudo_bytes).hexdigest()
                    
                    try:
                        num_linhas = conteudo_bytes.decode('utf-8').count('\n') + 1
                    except UnicodeDecodeError:
                        num_linhas = conteudo_bytes.decode('latin-1').count('\n') + 1

                    dados_arquivo = {
                        'caminho': caminho_completo,
                        'nome': arquivo,
                        'num_linhas': num_linhas,
                        'tamanho_kb': tamanho_kb,
                        'data_modificacao': datetime.fromtimestamp(mod_timestamp),
                        'md5_hash': md5_hash
                    }

                    # Lógica para manter apenas o arquivo mais antigo em caso de duplicação
                    if md5_hash not in arquivos_processados_md5 or mod_timestamp < arquivos_processados_md5[md5_hash]['mod_timestamp']:
                        arquivos_processados_md5[md5_hash] = {
                            'mod_timestamp': mod_timestamp,
                            'dados': dados_arquivo
                        }

                except Exception as e:
                    print(f"  - Aviso: Não foi possível processar '{caminho_completo}'. Erro: {e}")
        
        self.dados_arquivos = [val['dados'] for val in arquivos_processados_md5.values()]
        print(f"Varredura concluída. {len(self.dados_arquivos)} arquivos .py únicos (versões mais antigas) encontrados.")

    def analisar_e_preparar_dataframe(self):
        """
        Converte os dados coletados para um DataFrame do pandas e o enriquece
        com colunas de tempo para análise.
        """
        if not self.dados_arquivos:
            print("Nenhum dado para analisar.")
            return False

        print("Preparando dados para análise...")
        self.df = pd.DataFrame(self.dados_arquivos)
        self.df['data_modificacao'] = pd.to_datetime(self.df['data_modificacao'])
        self.df = self.df.sort_values('data_modificacao').set_index('data_modificacao')

        # Enriquece o DataFrame com colunas de data/hora
        self.df['ano'] = self.df.index.year
        self.df['mes'] = self.df.index.month
        self.df['dia_semana'] = self.df.index.day_name()
        self.df['hora'] = self.df.index.hour
        
        # Garante a ordem correta para os dias da semana
        dias_ordem = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.df['dia_semana'] = pd.Categorical(self.df['dia_semana'], categories=dias_ordem, ordered=True)

        print("Análise de dados concluída.")
        return True

class GeradorDeGraficos:
    """
    Gera vários gráficos a partir de um DataFrame de análise de código.
    """
    def __init__(self, df, output_dir, base_dir_name):
        self.df = df
        self.output_dir = output_dir
        self.base_dir_name = base_dir_name
        self.imagens_geradas = []
        os.makedirs(self.output_dir, exist_ok=True)

    def _gerar_nome_arquivo(self, tipo_grafico):
        """Cria um nome de arquivo único e complexo."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        hash_obj = hashlib.sha1(f"{tipo_grafico}{self.base_dir_name}{timestamp}".encode())
        short_hash = hash_obj.hexdigest()[:8]
        return f"{tipo_grafico}_{timestamp}_{short_hash}.png"

    def _salvar_grafico(self, fig, nome_base):
        """Salva a figura e armazena o caminho."""
        nome_arquivo = self._gerar_nome_arquivo(nome_base)
        caminho_completo = os.path.join(self.output_dir, nome_arquivo)
        fig.savefig(caminho_completo, dpi=150, facecolor=fig.get_facecolor())
        plt.close(fig)
        self.imagens_geradas.append(nome_arquivo)
        print(f"  -> Gráfico salvo: {nome_arquivo}")

    def plotar_evolucao_loc_por_ano_area(self):
        """Gráfico de área empilhada: Linhas de código adicionadas por ano."""
        print("Gerando gráfico: Evolução de Linhas de Código por Ano...")
        loc_por_ano = self.df.groupby('ano')['num_linhas'].sum()
        
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.stackplot(loc_por_ano.index, loc_por_ano.values, alpha=0.8, color='#4ac3d4')

        ax.set_title('Evolução de Linhas de Código por Ano', fontsize=16, fontweight='bold')
        ax.set_ylabel('Linhas de Código Adicionadas')
        ax.set_xlabel('Ano')
        ax.grid(True, axis='y', linestyle='--', alpha=0.5)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{int(x/1000)}k'))
        ax.set_xlim(loc_por_ano.index.min(), loc_por_ano.index.max())
        
        self._salvar_grafico(fig, "evolucao_loc_anual")

    def plotar_crescimento_cumulativo_linha(self):
        """Gráfico de linha: Crescimento cumulativo de arquivos e linhas de código."""
        print("Gerando gráfico: Crescimento Cumulativo do Projeto...")
        df_resampled = self.df.resample('M').agg({
            'num_linhas': 'sum',
            'nome': 'count'
        }).rename(columns={'nome': 'num_arquivos'})

        df_resampled['loc_cumulativo'] = df_resampled['num_linhas'].cumsum()
        df_resampled['arquivos_cumulativo'] = df_resampled['num_arquivos'].cumsum()

        fig, ax1 = plt.subplots(figsize=(14, 7))

        # Eixo 1: Linhas de Código
        color1 = '#4ac3d4'
        ax1.plot(df_resampled.index, df_resampled['loc_cumulativo'], color=color1, label='Total de Linhas de Código', lw=2)
        ax1.set_xlabel('Data')
        ax1.set_ylabel('Linhas de Código Cumulativas', color=color1)
        ax1.tick_params(axis='y', labelcolor=color1)
        ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{int(x/1000)}k'))
        
        # Eixo 2: Arquivos
        ax2 = ax1.twinx()
        color2 = '#e57a35'
        ax2.plot(df_resampled.index, df_resampled['arquivos_cumulativo'], color=color2, label='Total de Arquivos', lw=2, linestyle='--')
        ax2.set_ylabel('Arquivos Cumulativos', color=color2)
        ax2.tick_params(axis='y', labelcolor=color2)

        ax1.set_title('Crescimento Cumulativo do Código-Fonte', fontsize=16, fontweight='bold')
        ax1.grid(True, axis='y', linestyle=':', alpha=0.5)
        fig.tight_layout()
        self._salvar_grafico(fig, "crescimento_cumulativo")

    def plotar_atividade_por_dia_semana_barra(self):
        """Gráfico de barras: Atividade por dia da semana."""
        print("Gerando gráfico: Atividade por Dia da Semana...")
        atividade_dia = self.df.groupby('dia_semana')['num_linhas'].sum()
        
        fig, ax = plt.subplots(figsize=(12, 7))
        atividade_dia.plot(kind='bar', ax=ax, color='#57a661', alpha=0.85)

        ax.set_title('Total de Linhas de Código por Dia da Semana', fontsize=16, fontweight='bold')
        ax.set_xlabel('Dia da Semana')
        ax.set_ylabel('Total de Linhas de Código')
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{int(x/1000)}k'))
        plt.xticks(rotation=45, ha='right')
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        fig.tight_layout()
        self._salvar_grafico(fig, "atividade_dia_semana")

    def plotar_atividade_por_hora_barra(self):
        """Gráfico de barras: Atividade por hora do dia."""
        print("Gerando gráfico: Atividade por Hora do Dia...")
        atividade_hora = self.df.groupby('hora')['num_linhas'].sum().reindex(range(24), fill_value=0)
        
        fig, ax = plt.subplots(figsize=(14, 7))
        atividade_hora.plot(kind='bar', ax=ax, color='#f0d43d', alpha=0.9)

        ax.set_title('Total de Linhas de Código por Hora do Dia', fontsize=16, fontweight='bold')
        ax.set_xlabel('Hora do Dia (0-23)')
        ax.set_ylabel('Total de Linhas de Código')
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{int(x/1000)}k'))
        plt.xticks(rotation=0)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        fig.tight_layout()
        self._salvar_grafico(fig, "atividade_hora_dia")
    
    def plotar_distribuicao_por_ano_donut(self):
        """Gráfico de Donut: Distribuição de arquivos por ano."""
        print("Gerando gráfico: Distribuição de Arquivos por Ano...")
        dist_ano = self.df.groupby('ano')['nome'].count()

        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Cores customizadas
        colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(dist_ano)))

        wedges, texts, autotexts = ax.pie(
            dist_ano, 
            labels=dist_ano.index, 
            autopct='%1.1f%%', 
            startangle=90, 
            colors=colors,
            pctdistance=0.85,
            wedgeprops=dict(width=0.4, edgecolor=DARK_BG_COLOR)
        )
        
        plt.setp(autotexts, size=10, weight="bold", color='white')
        plt.setp(texts, size=12, color=TEXT_COLOR)
        ax.set_title('Distribuição de Arquivos Únicos por Ano', fontsize=16, fontweight='bold')
        
        self._salvar_grafico(fig, "distribuicao_anual_donut")

    def plotar_top_10_por_linhas_hbar(self):
        """Gráfico de barras horizontal: Top 10 arquivos por número de linhas."""
        print("Gerando gráfico: Top 10 Arquivos por Linhas...")
        top_10_linhas = self.df.nlargest(10, 'num_linhas')
        
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.barh(top_10_linhas['nome'], top_10_linhas['num_linhas'], color='#c83737', alpha=0.85)

        ax.invert_yaxis() # O maior fica no topo
        ax.set_title('Top 10 Arquivos por Número de Linhas', fontsize=16, fontweight='bold')
        ax.set_xlabel('Número de Linhas')
        ax.grid(axis='x', linestyle='--', alpha=0.4)
        
        # Adiciona os valores nas barras
        for i, v in enumerate(top_10_linhas['num_linhas']):
            ax.text(v + 5, i, str(v), color=TEXT_COLOR, va='center')
        
        fig.tight_layout()
        self._salvar_grafico(fig, "top10_por_linhas")
        
    def plotar_top_10_por_tamanho_hbar(self):
        """Gráfico de barras horizontal: Top 10 arquivos por tamanho em KB."""
        print("Gerando gráfico: Top 10 Arquivos por Tamanho...")
        top_10_tamanho = self.df.nlargest(10, 'tamanho_kb')
        
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.barh(top_10_tamanho['nome'], top_10_tamanho['tamanho_kb'], color='#d94444', alpha=0.85)

        ax.invert_yaxis()
        ax.set_title('Top 10 Arquivos por Tamanho (KB)', fontsize=16, fontweight='bold')
        ax.set_xlabel('Tamanho (KB)')
        ax.grid(axis='x', linestyle='--', alpha=0.4)
        
        for i, v in enumerate(top_10_tamanho['tamanho_kb']):
            ax.text(v + 1, i, f'{v:.1f} KB', color=TEXT_COLOR, va='center')

        fig.tight_layout()
        self._salvar_grafico(fig, "top10_por_tamanho")

    def gerar_todos_os_graficos(self):
        """Executa todos os métodos de plotagem."""
        print("\n--- Iniciando Geração de Gráficos ---")
        self.plotar_evolucao_loc_por_ano_area()
        self.plotar_crescimento_cumulativo_linha()
        self.plotar_atividade_por_dia_semana_barra()
        self.plotar_atividade_por_hora_barra()
        self.plotar_distribuicao_por_ano_donut()
        self.plotar_top_10_por_linhas_hbar()
        self.plotar_top_10_por_tamanho_hbar()
        print("--- Geração de Gráficos Concluída ---\n")
        return self.imagens_geradas

def gerar_relatorio_html(imagens, output_dir, dir_analisado, df_stats):
    """Gera um arquivo HTML para exibir todos os gráficos e estatísticas."""
    print("Gerando relatório HTML...")
    nome_arquivo = "relatorio_analise_codigo.html"
    caminho_completo = os.path.join(output_dir, nome_arquivo)

    # Coleta de estatísticas gerais
    total_arquivos = len(df_stats)
    total_linhas = df_stats['num_linhas'].sum()
    total_kb = df_stats['tamanho_kb'].sum()
    data_inicio = df_stats.index.min().strftime('%d/%m/%Y')
    data_fim = df_stats.index.max().strftime('%d/%m/%Y')

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Relatório de Análise de Código</title>
        <style>
            body {{ font-family: sans-serif; background-color: {DARK_BG_COLOR}; color: {TEXT_COLOR}; margin: 0; padding: 20px; }}
            h1, h2 {{ color: {TEXT_COLOR}; border-bottom: 2px solid {GRID_COLOR}; padding-bottom: 10px; }}
            .container {{ max-width: 1200px; margin: auto; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(500px, 1fr)); gap: 20px; }}
            .chart-box {{ background-color: #2a2a2a; border: 1px solid {GRID_COLOR}; border-radius: 8px; padding: 15px; }}
            img {{ max-width: 100%; height: auto; border-radius: 4px; }}
            .stats-box {{ background-color: #2a2a2a; border: 1px solid {GRID_COLOR}; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
            .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }}
            .stat {{ text-align: center; }}
            .stat h3 {{ margin: 0 0 5px 0; color: #4ac3d4; }}
            .stat p {{ margin: 0; font-size: 1.5em; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Relatório de Análise de Código Python</h1>
            <p>Diretório Analisado: <code>{dir_analisado}</code></p>
            
            <div class="stats-box">
                <h2>Resumo Geral</h2>
                <div class="stats-grid">
                    <div class="stat"><h3>Total de Arquivos Únicos</h3><p>{total_arquivos:,}</p></div>
                    <div class="stat"><h3>Total de Linhas</h3><p>{total_linhas:,}</p></div>
                    <div class="stat"><h3>Tamanho Total</h3><p>{total_kb/1024:.2f} MB</p></div>
                    <div class="stat"><h3>Período Analisado</h3><p>{data_inicio} - {data_fim}</p></div>
                </div>
            </div>

            <h2>Visualizações Gráficas</h2>
            <div class="grid">
    """
    for img in imagens:
        titulo = img.split('_')[0].replace('-', ' ').title()
        html += f"""
                <div class="chart-box">
                    <h3>{titulo}</h3>
                    <img src="{img}" alt="{titulo}">
                </div>
        """
    html += """
            </div>
        </div>
    </body>
    </html>
    """
    with open(caminho_completo, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Relatório salvo em: '{os.path.abspath(caminho_completo)}'")

def main():
    """Função principal para orquestrar a análise e geração de gráficos."""
    print("--- Gerador de Análise Gráfica de Código Python ---")
    
    diretorio_alvo = input(f"Digite o caminho do diretório a ser analisado (ou Enter para o padrão: {DEFAULT_DIR}): ").strip()
    if not diretorio_alvo:
        diretorio_alvo = DEFAULT_DIR
    
    if not os.path.isdir(diretorio_alvo):
        print(f"Erro: O diretório '{diretorio_alvo}' não existe ou não é válido.")
        return

    try:
        # 1. Análise
        analisador = AnalisadorDeCodigo(diretorio_alvo)
        analisador.varrer_arquivos()
        if not analisador.analisar_e_preparar_dataframe():
            print("Nenhum arquivo Python foi encontrado para análise. O script será encerrado.")
            return

        # 2. Geração de Gráficos
        base_dir_name = os.path.basename(os.path.normpath(diretorio_alvo))
        gerador_graficos = GeradorDeGraficos(analisador.df, OUTPUT_DIR, base_dir_name)
        imagens_geradas = gerador_graficos.gerar_todos_os_graficos()
        
        # 3. Geração do Relatório HTML
        if imagens_geradas:
            gerar_relatorio_html(imagens_geradas, OUTPUT_DIR, diretorio_alvo, analisador.df)
        else:
            print("Nenhuma imagem foi gerada, o relatório HTML não será criado.")

    except Exception as e:
        print(f"\nOcorreu um erro inesperado durante a execução: {e}")

if __name__ == "__main__":
    main()
