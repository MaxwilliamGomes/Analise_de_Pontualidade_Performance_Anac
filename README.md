# Desempenho por Aeroporto – Atrasos e Impacto

## Cliente: Agência Nacional de Aviação Civil (Anac)
## Objetivo: Avaliar o desempenho dos aeroportos brasileiros em relação a atrasos e pontualidade para melhorar a eficiência operacional e a experiência dos passageiros.

## Problema de Negócio

### A Anac identificou um aumento no número de reclamações de passageiros devido a atrasos frequentes em voos internacionais. 

### A agência quer entender:

### Quais aeroportos apresentam maior incidência de atrasos na partida e na chegada?
### Os atrasos estão concentrados em horários ou companhias específicas?
### Qual o impacto dos atrasos na eficiência operacional dos aeroportos e na conectividade de voos?
### O objetivo é identificar padrões e recomendar melhorias para reduzir atrasos, minimizar custos operacionais e melhorar a satisfação dos passageiros.




## Estrutura do projeto

```mermaid
graph TD;
    A(["🎬 Início"]) --> B(["🐍 Web Scraping com Python"]) 
    B -->|📂 Extrai os CSV| C(["🐘 Armazena no PostgreSQL"])
    C -->|📥 Carrega Dados Brutos| D(["⚙️ dbt - Transformação"])
    D -->|🥈 Camada Silver| E(["🥇 Camada Gold"])
    E -->|📊 Fonte de Dados| F(["📈 Dashboard no Power BI"])
    F --> ["🏁 FIM"];
```