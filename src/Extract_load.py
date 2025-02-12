# import
import requests
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import glob


# import das minhas variáveis de ambiente

load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)



# Fazer o webscraping dos arquivos


## Função para baixar arquivos
def baixar_arquivo(url, endereco):
 """
    Fazendo o download dos arquivos e salvando no endereço especificado.
    """
 resposta = requests.get(url)
 if resposta.status_code == requests.codes.ok:
   with open(endereco , 'wb') as novo_arquivo:
       novo_arquivo.write(resposta.content)
   print(f"Download finalizado. Salvo em: {endereco}")
 else:
   resposta.raise_for_status()

  
## Função para verificar se um arquivo já existe
def verificar_arquivo_existe(endereco):
    """
    Verifica se um arquivo já existe no diretório.
    """
    return os.path.exists(endereco)



if __name__ == "__main__":
  BASE_URL = "https://siros.anac.gov.br/siros/registros/diversos/vra/2024/VRA_2024_{:02d}.csv"
  DATASET_DIR = 'dataset'
  TABELA = DB_NAME

  ## Criando diretório caso não exista
  os.makedirs(DATASET_DIR, exist_ok=True)

# Faz o download dos arquivos
  for i in range(1 , 13):
   nome_arquivo = os.path.join(DATASET_DIR, f'VRA_2024_{i:02d}.csv')

   ## Verifica se o arquivo já existe
   if verificar_arquivo_existe(nome_arquivo):
        print(f"Arquivo já existe: {nome_arquivo}. Pulando download.")
        continue
   
   
   baixar_arquivo(BASE_URL.format(i), nome_arquivo)



# Caminho para os arquivos CSV
caminho = "C:/Users/PICHAU/Documents/Analise_de_Pontualidade_Performance_Anac/dataset/"

# Listar todos os arquivos CSV no diretório que começam com "VRA_2024"
arquivos = glob.glob(caminho + "VRA_2024_*.csv")

# Carregar e concatenar os arquivos em um único DataFrame
dataframe = pd.concat((pd.read_csv(f, delimiter=';') for f in arquivos), ignore_index=True)
    
    
    
# Carrega os dados no banco de dados, usando o schema especificado
    
def salvar_no_postgres(df, schema='public'):
    
  df.to_sql(
              TABELA,
              engine,  
              if_exists="append",
              index=True,
              schema = schema)


#Carrega os arquivos CSV no banco de dados
salvar_no_postgres(
        dataframe,
        schema=DB_SCHEMA
    )