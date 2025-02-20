# ✈️ Desempenho por Aeroporto – Atrasos e Impacto  
**por [Maxwilliam Gomes](https://www.linkedin.com/in/maxwilliam-gomes-74b01716a/)**  
[![LinkedIn](https://img.shields.io/badge/-Conectar_no_LinkedIn-%230A66C2)](https://www.linkedin.com/in/maxwilliam-gomes-74b01716a/)
[![Email](https://img.shields.io/badge/-Enviar_Email-%23EA4335)](mailto:maxwilliamgomes@gmail.com)
[![Análise Completa](https://img.shields.io/badge/-Ver_Extract_Load-%2300B388)](https://github.com/MaxwilliamGomes/Analise_de_Pontualidade_Performance_Anac/blob/main/src/Extract_load.py)

---

## 🚀 **Visão Geral do Projeto**  
Este projeto foi desenvolvido para a **Agência Nacional de Aviação Civil (Anac)** com o objetivo de avaliar o desempenho dos aeroportos brasileiros em relação a **atrasos e pontualidade**. Utilizando técnicas de **web scraping**, **ETL** e **análise de dados**, o estudo visa identificar padrões de atrasos, impactos na eficiência operacional e oportunidades de melhoria para a experiência dos passageiros.  

## **Problema de Negócio**

A Anac identificou um aumento no número de reclamações de passageiros devido a atrasos frequentes em voos internacionais. 

## **A agência quer entender:**

Quais aeroportos apresentam maior incidência de atrasos na partida e na chegada?
Os atrasos estão concentrados em horários ou companhias específicas?
Qual o impacto dos atrasos na eficiência operacional dos aeroportos e na conectividade de voos?


O objetivo é identificar padrões e recomendar melhorias para reduzir atrasos, minimizar custos operacionais e melhorar a satisfação dos passageiros.

---

**Resultado Chave:**

---

## 📊 **Metodologia**  
### **Passo a Passo**  
1. **Coleta de Dados:**  
   - **Web Scraping** com Python para extrair dados de atrasos e pontualidade de voos.  
   - Armazenamento dos dados brutos em um banco **PostgreSQL**.  
2. **Transformação de Dados:**  
   - Utilização do **dbt** para criar camadas de dados (Silver e Gold).  
   - Limpeza, normalização e enriquecimento dos dados.  
3. **Análise e Visualização:**  
   - Criação de um **dashboard no Power BI** para visualização dos resultados.  
   - Identificação de padrões de atrasos por aeroporto, horário e companhia aérea.  

### 📈 **Resultados Detalhados**  
| Métrica                        | Resultado             | Impacto                            |  
|--------------------------------|-----------------------|------------------------------------|  
| Aeroportos com Mais Atrasos    | Aeroporto X, Y, Z     | **---**                            |  
| Horários de Pico de Atrasos    | ----                  | **---**                            |  
| Redução de Custos Operacionais | Estimativa de **???** | **---**                            |  

---

## 🛠️ **Tecnologias Utilizadas**  
<div align="center">  
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">  
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">  
  <img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white" alt="dbt">  
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI">  
</div>  

---

## Estrutura do projeto

```mermaid
flowchart TD
    A["🎬 Início"] --> B["🐍 Web Scraping com Python"]
    B -->|📂 Extrai os CSV| C["🐘 Armazena no PostgreSQL"]
    C -->|📥 Carrega Dados Brutos| D["⚙️ dbt - Transformação"]
    D -->|🥈 Camada Silver| E["🥇 Camada Gold"]
    E -->|📊 Fonte de Dados| F["📈 Dashboard no Power BI"]
    F --> G["🏁 FIM"];
```

---

## 📂 **Estrutura do Repositório**  
```plaintext
Analise_de_Pontualidade_Performance_Anac/  
├── src/                  
│   └── Extract_load.py   # Script de web scraping e ETL  
├── data/                  
│   ├── raw/              # Dados brutos (CSV)  
│   └── processed/        # Dados tratados  
├── dbt/                  # Projeto dbt para transformação  
├── dashboards/           # Arquivos do Power BI  
├── README.md             # Documentação  