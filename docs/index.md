# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).


```mermaid
A["🎬 Início"] --> B["🐍 Web Scraping com Python"]
    B -->|📂 Extrai os CSV| C["🐘 Armazena no PostgreSQL"]
    C -->|📥 Carrega Dados Brutos| D["⚙️ dbt - Transformação"]
    D -->|🥈 Camada Silver| E["🥇 Camada Gold"]
    E -->|📊 Fonte de Dados| F["📈 Dashboard no Power BI"]
    F --> G["🏁 FIM"];
```

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
