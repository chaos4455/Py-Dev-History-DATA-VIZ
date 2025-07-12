<div align="center">
  <img src="https://raw.githubusercontent.com/chaos4455/Py-Dev-History-DATA-VIZ/main/assets/project_logo.png" alt="Project Logo" width="150"/>
  <h1>📊 Py-Dev-History-DATA-VIZ 📈</h1>
  <p>
    <strong>EN:</strong> A powerful tool to scan your local Python codebases and generate beautiful, insightful visualizations about their development history.
    <br>
    <strong>PT-BR:</strong> Uma poderosa ferramenta para escanear seus projetos Python locais e gerar visualizações ricas e detalhadas sobre o histórico de desenvolvimento.
  </p>

  <!-- Shields/Badges -->
  <p>
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python" alt="Python Version">
    <img src="https://img.shields.io/badge/Made%20with-Pandas-e1523d.svg?style=for-the-badge&logo=pandas" alt="Made with Pandas">
    <img src="https://img.shields.io/badge/Visualized%20with-Matplotlib-yellow.svg?style=for-the-badge&logo=matplotlib" alt="Visualized with Matplotlib">
    <img src="https://img.shields.io/github/last-commit/chaos4455/Py-Dev-History-DATA-VIZ?style=for-the-badge&logo=github&color=57a661" alt="Last Commit">
    <img src="https://img.shields.io/badge/License-MIT-orange.svg?style=for-the-badge" alt="License: MIT">
  </p>
</div>

---

<details>
<summary><strong>🌐 Table of Contents / Índice (Click to expand)</strong></summary>

- [🇧🇷 Em Português](#-em-português)
  - [🎯 Sobre o Projeto](#-sobre-o-projeto)
  - [✨ Principais Funcionalidades](#-principais-funcionalidades)
  - [🖼️ Exemplo do Relatório Gerado](#️-exemplo-do-relatório-gerado)
  - [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
  - [🚀 Como Começar](#-como-começar)
  - [🎨 Customização e Aprimoramento](#-customização-e-aprimoramento)
  - [🧠 Como Funciona (Detalhes Técnicos)](#-como-funciona-detalhes-técnicos)
- [🇺🇸 In English](#-in-english)
  - [🎯 About The Project](#-about-the-project)
  - [✨ Key Features](#-key-features)
  - [🖼️ Sample Report Output](#️-sample-report-output)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [🚀 Getting Started](#-getting-started)
  - [🎨 Customization and Enhancement](#-customization-and-enhancement)
  - [🧠 How It Works (Technical Details)](#-how-it-works-technical-details)
- [🤝 Como Contribuir / How to Contribute](#-como-contribuir--how-to-contribute)
- [📜 Licença / License](#-licença--license)
- [📞 Contato / Contact](#-contato--contact)

</details>

---

## 🇧🇷 Em Português

### 🎯 Sobre o Projeto

Você já se perguntou como seus projetos de software evoluíram ao longo do tempo? Em que dias da semana você é mais produtivo? Quais são os arquivos mais "pesados" do seu repositório?

O **Py-Dev-History-DATA-VIZ** nasceu para responder a essas perguntas. Ele é um script em Python que analisa um diretório de projetos, varre todos os arquivos `.py` e gera um **relatório HTML completo e visual** com gráficos que contam a história do seu código. A ferramenta utiliza os metadados dos arquivos (como a data da última modificação) para criar uma linha do tempo do desenvolvimento, oferecendo insights valiosos sobre padrões de trabalho, crescimento do projeto e complexidade do código.

A principal inovação é a **deduplicação inteligente**: se você tem cópias do mesmo arquivo em diferentes lugares, a ferramenta considera apenas a versão **mais antiga**, garantindo que a análise histórica seja precisa e represente o verdadeiro ponto de origem do código.

### ✨ Principais Funcionalidades

-   🔍 **Varredura Recursiva:** Analisa subpastas, ignorando inteligentemente diretórios comuns como `.venv`, `.git`, e `__pycache__`.
-   🧠 **Deduplicação por Conteúdo:** Usa hashes MD5 para identificar arquivos idênticos e mantém apenas a versão com a data de modificação mais antiga para uma análise histórica fiel.
-   📊 **Dashboard em HTML:** Gera um único arquivo `relatorio_analise_codigo.html` com um resumo estatístico e todos os gráficos, perfeito para compartilhar e analisar.
-   🎨 **Gráficos Estilizados:** Visualizações em *dark mode*, geradas com Matplotlib, que são tanto informativas quanto agradáveis de se ver.
-   📈 **Análise de Evolução:** Gráfico de área que mostra o crescimento de Linhas de Código (LoC) ano a ano.
-   💹 **Crescimento Cumulativo:** Gráfico de linha dupla que acompanha o aumento do número de arquivos e do total de LoC ao longo do tempo.
-   📅 **Padrões de Trabalho:** Gráficos de barra que revelam os dias da semana e as horas do dia mais produtivas.
-   🍩 **Distribuição Anual:** Gráfico de rosca (donut chart) que mostra a proporção de arquivos criados em cada ano.
-   🏆 **Ranking de Arquivos:** Gráficos que listam o Top 10 maiores arquivos por número de linhas e por tamanho em KB.

### 🖼️ Exemplo do Relatório Gerado

Ao executar o script, ele criará um diretório `analise_codigo_output/` contendo um arquivo `relatorio_analise_codigo.html`. Ao abri-lo, você verá um dashboard semelhante a este:

<div align="center">
  <img src="https://raw.githubusercontent.com/chaos4455/Py-Dev-History-DATA-VIZ/main/assets/sample_report.gif" alt="Exemplo do Relatório HTML" />
  <p><em>Animação demonstrando o relatório HTML gerado.</em></p>
</div>

### 🛠️ Tecnologias Utilizadas

Este projeto foi construído com algumas das bibliotecas mais poderosas do ecossistema Python para análise de dados e visualização:

| Tecnologia | Descrição |
| :--- | :--- |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/> | **Python** | A linguagem base para toda a lógica do projeto. |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original-wordmark.svg" alt="Pandas" width="40" height="40"/> | **Pandas** | Utilizada para manipulação, agregação e análise eficiente dos dados coletados dos arquivos. |
| <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="Matplotlib" width="40" height="40"/> | **Matplotlib** | A biblioteca central para a criação de todos os gráficos estáticos e customizados. |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="NumPy" width="40" height="40"/> | **NumPy** | Usado em conjunto com Matplotlib para operações numéricas e de cores. |

### 🚀 Como Começar

Siga estes passos simples para rodar a análise em seus próprios projetos.

1.  **Pré-requisitos:**
    *   Python 3.7 ou superior instalado.
    *   Pip (gerenciador de pacotes do Python).

2.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/chaos4455/Py-Dev-History-DATA-VIZ.git
    cd Py-Dev-History-DATA-VIZ
    ```

3.  **Instale as Dependências:**
    (É uma boa prática criar um ambiente virtual primeiro: `python -m venv venv` e ativá-lo)
    ```bash
    pip install pandas matplotlib numpy
    ```

4.  **Execute o Script:**
    Rode o script principal a partir do seu terminal:
    ```bash
    python main.py
    ```
    O script pedirá que você insira o caminho do diretório que deseja analisar. Se você apenas pressionar `Enter`, ele usará o diretório padrão definido na variável `DEFAULT_DIR` dentro do script.

5.  **Veja os Resultados:**
    Após a execução, uma nova pasta chamada `analise_codigo_output` será criada. Dentro dela, você encontrará as imagens dos gráficos e o arquivo `relatorio_analise_codigo.html`. Abra este arquivo em seu navegador para ver o dashboard completo!

### 🎨 Customização e Aprimoramento

A ferramenta foi projetada para ser flexível. Veja como você pode adaptá-la:

*   **Analisar Outros Tipos de Arquivo:**
    O padrão é analisar apenas arquivos `.py`. Para incluir outras extensões (ex: `.js`, `.html`, `.css`), localize esta linha no método `varrer_arquivos` da classe `AnalisadorDeCodigo`:
    ```python
    if not arquivo.endswith(".py"):
        continue
    ```
    Substitua-a para incluir as extensões desejadas. A melhor forma é usar uma tupla:
    ```python
    # Exemplo para analisar Python, JavaScript e CSS
    EXTENSOES_PERMITIDAS = ('.py', '.js', '.css')
    if not arquivo.endswith(EXTENSOES_PERMITIDAS):
        continue
    ```

*   **Ignorar Mais Pastas:**
    Se você tem pastas específicas do seu projeto que devem ser ignoradas, basta adicionar o nome delas (em minúsculas) ao `set` `PASTAS_IGNORADAS` no início do script.
    ```python
    PASTAS_IGNORADAS = set([
        'venv', '.venv', 'minha_pasta_customizada', ...
    ])
    ```

*   **Mudar o Estilo dos Gráficos:**
    Todas as configurações de estilo (cores de fundo, texto, grades) estão centralizadas no início do script. Sinta-se à vontade para experimentar novos valores hexadecimais e criar um tema que seja a sua cara!

### 🧠 Como Funciona (Detalhes Técnicos)

O fluxo de operação do script é dividido em três partes principais:

1.  **`AnalisadorDeCodigo` (A Classe de Coleta):**
    *   **Varredura (`os.walk`):** Percorre recursivamente o diretório alvo. Em cada passo, ele poda a lista de subpastas para não entrar em diretórios ignorados.
    *   **Filtragem e Coleta:** Para cada arquivo com a extensão permitida (`.py`), ele coleta metadados: caminho, tamanho e data de modificação.
    *   **Hashing e Deduplicação:** O conteúdo do arquivo é lido em bytes para calcular um hash MD5. Este hash atua como uma "impressão digital" do conteúdo. Um dicionário rastreia os hashes já vistos. Se um novo arquivo com o mesmo hash é encontrado, suas datas de modificação são comparadas. O script **sempre mantém a versão com a data mais antiga**, que representa o "commit" ou salvamento original daquele código.
    *   **Preparação do DataFrame:** Os dados únicos coletados são carregados em um DataFrame do Pandas. Novas colunas (ano, mês, dia da semana, hora) são extraídas da data de modificação para facilitar a agregação.

2.  **`GeradorDeGraficos` (A Classe de Visualização):**
    *   Recebe o DataFrame preparado.
    *   Cada método `plotar_*` é responsável por um gráfico específico.
    *   Ele usa `groupby()` do Pandas para agregar os dados (ex: somar linhas de código por ano, contar arquivos por dia da semana).
    *   Usa Matplotlib para desenhar os gráficos, aplicando as configurações de estilo (dark mode, cores, etc.).
    *   Salva cada gráfico como um arquivo `.png` na pasta de saída.

3.  **Função `main` e `gerar_relatorio_html` (O Orquestrador):**
    *   A função `main` gerencia todo o processo: pede o input do usuário, cria as instâncias das classes e chama os métodos na ordem correta.
    *   Ao final, `gerar_relatorio_html` pega a lista de imagens geradas, calcula algumas estatísticas gerais (total de arquivos, total de linhas) e monta uma string HTML.
    *   Esta string HTML usa CSS inline simples para criar o layout do dashboard e incorpora as imagens dos gráficos, resultando em um relatório final autocontido.

---

## 🇺🇸 In English

### 🎯 About The Project

Have you ever wondered how your software projects have evolved over time? On which days of the week are you most productive? What are the "heaviest" files in your repository?

**Py-Dev-History-DATA-VIZ** was created to answer these questions. It's a Python script that analyzes a project directory, scans all `.py` files, and generates a **complete and visual HTML report** with charts that tell the story of your code. The tool uses file metadata (like the last modification date) to create a development timeline, offering valuable insights into work patterns, project growth, and code complexity.

The key innovation is its **intelligent deduplication**: if you have copies of the same file in different places, the tool only considers the **oldest** version, ensuring the historical analysis is accurate and represents the true origin point of the code.

### ✨ Key Features

-   🔍 **Recursive Scanning:** Analyzes subfolders, intelligently ignoring common directories like `.venv`, `.git`, and `__pycache__`.
-   🧠 **Content-based Deduplication:** Uses MD5 hashes to identify identical files and keeps only the version with the oldest modification date for a faithful historical analysis.
-   📊 **HTML Dashboard:** Generates a single `relatorio_analise_codigo.html` file with a statistical summary and all charts, perfect for sharing and analysis.
-   🎨 **Stylish Charts:** Dark mode visualizations, generated with Matplotlib, that are both informative and aesthetically pleasing.
-   📈 **Evolution Analysis:** An area chart showing the growth of Lines of Code (LoC) year by year.
-   💹 **Cumulative Growth:** A dual-axis line chart tracking the increase in the number of files and total LoC over time.
-   📅 **Work Patterns:** Bar charts that reveal the most productive days of the week and hours of the day.
-   🍩 **Annual Distribution:** A donut chart showing the proportion of files created each year.
-   🏆 **File Ranking:** Charts listing the Top 10 largest files by line count and by size in KB.

### 🖼️ Sample Report Output

When you run the script, it will create an `analise_codigo_output/` directory containing an `relatorio_analise_codigo.html` file. Opening it will reveal a dashboard similar to this:

<div align="center">
  <img src="https://raw.githubusercontent.com/chaos4455/Py-Dev-History-DATA-VIZ/main/assets/sample_report.gif" alt="Sample HTML Report" />
  <p><em>Animation demonstrating the generated HTML report.</em></p>
</div>

### 🛠️ Technologies Used

This project was built with some of the most powerful libraries in the Python ecosystem for data analysis and visualization:

| Technology | Description |
| :--- | :--- |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/> | **Python** | The base language for all project logic. |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original-wordmark.svg" alt="Pandas" width="40" height="40"/> | **Pandas** | Used for efficient manipulation, aggregation, and analysis of the collected file data. |
| <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="Matplotlib" width="40" height="40"/> | **Matplotlib** | The core library for creating all static and customized charts. |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="NumPy" width="40" height="40"/> | **NumPy** | Used in conjunction with Matplotlib for numerical and color operations. |

### 🚀 Getting Started

Follow these simple steps to run the analysis on your own projects.

1.  **Prerequisites:**
    *   Python 3.7 or higher installed.
    *   Pip (Python's package manager).

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/chaos4455/Py-Dev-History-DATA-VIZ.git
    cd Py-Dev-History-DATA-VIZ
    ```

3.  **Install Dependencies:**
    (It's good practice to create a virtual environment first: `python -m venv venv` and activate it)
    ```bash
    pip install pandas matplotlib numpy
    ```

4.  **Run the Script:**
    Run the main script from your terminal:
    ```bash
    python main.py
    ```
    The script will prompt you to enter the path of the directory you want to analyze. If you just press `Enter`, it will use the default directory defined in the `DEFAULT_DIR` variable within the script.

5.  **View the Results:**
    After execution, a new folder named `analise_codigo_output` will be created. Inside it, you will find the chart images and the `relatorio_analise_codigo.html` file. Open this file in your browser to see the full dashboard!

### 🎨 Customization and Enhancement

The tool was designed to be flexible. Here’s how you can adapt it:

*   **Analyze Other File Types:**
    By default, it only analyzes `.py` files. To include other extensions (e.g., `.js`, `.html`, `.css`), locate this line in the `varrer_arquivos` method of the `AnalisadorDeCodigo` class:
    ```python
    if not arquivo.endswith(".py"):
        continue
    ```
    Replace it to include your desired extensions. The best way is to use a tuple:
    ```python
    # Example to analyze Python, JavaScript, and CSS
    ALLOWED_EXTENSIONS = ('.py', '.js', '.css')
    if not arquivo.endswith(ALLOWED_EXTENSIONS):
        continue
    ```

*   **Ignore More Folders:**
    If you have project-specific folders that should be ignored, simply add their names (in lowercase) to the `PASTAS_IGNORADAS` set at the beginning of the script.
    ```python
    PASTAS_IGNORADAS = set([
        'venv', '.venv', 'my_custom_folder', ...
    ])
    ```

*   **Change Chart Styles:**
    All style settings (background colors, text, grids) are centralized at the beginning of the script. Feel free to experiment with new hex values and create a theme that suits you!

### 🧠 How It Works (Technical Details)

The script's operational flow is divided into three main parts:

1.  **`AnalisadorDeCodigo` (The Collector Class):**
    *   **Scanning (`os.walk`):** Recursively traverses the target directory. At each step, it prunes the subfolder list to avoid entering ignored directories.
    *   **Filtering and Collection:** For each file with an allowed extension (`.py`), it collects metadata: path, size, and modification date.
    *   **Hashing and Deduplication:** The file's content is read in bytes to calculate an MD5 hash. This hash acts as a "fingerprint" of the content. A dictionary tracks already seen hashes. If a new file with the same hash is found, their modification dates are compared. The script **always keeps the version with the older date**, representing the original "commit" or save of that code.
    *   **DataFrame Preparation:** The collected unique data is loaded into a Pandas DataFrame. New columns (year, month, day of the week, hour) are extracted from the modification date to facilitate aggregation.

2.  **`GeradorDeGraficos` (The Visualization Class):**
    *   Receives the prepared DataFrame.
    *   Each `plotar_*` method is responsible for a specific chart.
    *   It uses Pandas' `groupby()` to aggregate the data (e.g., summing lines of code by year, counting files by day of the week).
    *   It uses Matplotlib to draw the charts, applying the style settings (dark mode, colors, etc.).
    *   Saves each chart as a `.png` file in the output folder.

3.  **`main` function and `gerar_relatorio_html` (The Orchestrator):**
    *   The `main` function manages the entire process: it asks for user input, creates instances of the classes, and calls the methods in the correct order.
    *   Finally, `gerar_relatorio_html` takes the list of generated images, calculates some general statistics (total files, total lines), and assembles an HTML string.
    *   This HTML string uses simple inline CSS to create the dashboard layout and embeds the chart images, resulting in a self-contained final report.

---

## 🤝 Como Contribuir / How to Contribute

Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Faça um Fork do projeto (Fork the Project)
2.  Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Faça o Commit de suas alterações (`git commit -m 'Add some AmazingFeature'`)
4.  Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5.  Abra um Pull Request

---

## 📜 Licença / License

Distribuído sob a Licença MIT. Veja `LICENSE` para mais informações.
<br>
Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <h3>📞 Contato / Contact</h3>
  <p>Elias Andrade - replika ai solutions</p>
  <p>Maringá - Paraná - Brasil</p>
  <p>
    <a href="https://www.linkedin.com/in/itilmgf/" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
    </a>
    <a href="https://wa.me/5511913353137" target="_blank">
      <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/>
    </a>
  </p>
  <p>Tem uma ideia para melhorar o projeto ou quer discutir uma aplicação customizada? Entre em contato!</p>
</div>
