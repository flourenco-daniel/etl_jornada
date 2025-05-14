# etl_jornada

## Visão Geral

Este projeto consiste em uma pipeline ETL (Extração, Transformação e Carga) que coleta dados de preços do Bitcoin da API da Coinbase, transforma esses dados e os carrega em um banco de dados PostgreSQL. Os dados são então visualizados em um dashboard Streamlit.

## Objetivos

-   [x] Planejar o projeto
-   [x] Extrair dados do Bitcoin da API da Coinbase
-   [x] Criar um banco de dados PostgreSQL no Render
-   [x] Criar um dashboard Streamlit para visualizar os dados
-   [ ] Criar um agente de IA (em desenvolvimento)

## Diagrama da Pipeline

O diagrama da pipeline foi criado usando o Excalidraw e pode ser visualizado [aqui](https://excalidraw.com/).

## Tecnologias Utilizadas

-   **Linguagem de Programação:** Python
-   **API:** Coinbase API ([https://api.coinbase.com/v2/prices/spot](https://api.coinbase.com/v2/prices/spot))
-   **Banco de Dados:** PostgreSQL (hospedado no Render)
-   **Conector PostgreSQL:** Psycopg2
-   **Framework Web:** Streamlit
-   **ORM:** SQLAlchemy
-   **Gerenciamento de Variáveis de Ambiente:** python-dotenv
-   **Agendamento:** (Implícito no script `sql.py` com `time.sleep`)

## Estrutura do Projeto

etl_jornada/
├── dashboard/
│ └── dashboard.py # Código do dashboard Streamlit
├── pipeline/
│ ├── nosql.py # Pipeline ETL para TinyDB (descontinuado)
│ └── sql.py # Pipeline ETL para PostgreSQL
├── .env # Variáveis de ambiente
├── README.md # Documentação do projeto
└── requirements.txt # Lista de dependências


## Configuração

### Pré-requisitos

-   Python 3.6+
-   Pip
-   Conta no [Render](https://render.com/) para hospedar o banco de dados PostgreSQL
-   Docker (opcional, para desenvolvimento local)

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone [URL do seu repositório]
    cd etl_jornada
    ```

2.  **Crie um ambiente virtual:**

    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**

    -   No Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

    -   No Windows:

        ```bash
        .\venv\Scripts\activate
        ```

4.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure as variáveis de ambiente:**

    -   Crie um arquivo `.env` na raiz do projeto.
    -   Adicione a URL de conexão do seu banco de dados PostgreSQL no Render:

        ```
        DATABASE_KEY="postgresql://usuario:senha@host:porta/banco_de_dados"
        ```

        Substitua `usuario`, `senha`, `host`, `porta` e `banco_de_dados` pelas suas credenciais.

## Execução

### Pipeline ETL (sql.py)

Este script extrai dados da API da Coinbase, transforma-os e os carrega no banco de dados PostgreSQL.

1.  **Execute o script:**

    ```bash
    python pipeline/sql.py
    ```

    O script será executado continuamente, coletando dados a cada 15 segundos.

### Dashboard Streamlit (dashboard.py)

Este script cria um dashboard interativo para visualizar os dados do Bitcoin.

1.  **Execute o script:**

    ```bash
    streamlit run dashboard/dashboard.py
    ```

2.  **Acesse o dashboard no seu navegador:**

    O Streamlit fornecerá um URL local para acessar o dashboard (geralmente `http://localhost:8501`).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

[MIT](LICENSE)
Observações
Substitua [URL do seu repositório] pelo URL real do seu repositório no GitHub.
Crie um arquivo LICENSE com a licença MIT (ou outra de sua preferência) e adicione-o ao repositório.
Certifique-se de que o arquivo .env esteja corretamente configurado com as suas credenciais do banco de dados.
Adicione o arquivo .env ao .gitignore para evitar o envio de informações sensíveis para o repositório.
Instale o python-dotenv com pip install python-dotenv.