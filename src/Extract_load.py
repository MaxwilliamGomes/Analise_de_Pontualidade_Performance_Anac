# import
import requests
import os
import pandas as pd
import sqlalchemy

# import das minhas variáveis de ambiente



# Fazer o webscraping dos arquivos

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

def verificar_arquivo_existe(endereco):
    """
    Verifica se um arquivo já existe no diretório.
    """
    return os.path.exists(endereco)

if __name__ == "__main__":
  BASE_URL = "https://siros.anac.gov.br/siros/registros/diversos/vra/2024/VRA_2024_{:02d}.csv"
  DATASET_DIR = 'dataset'

  ## Criando diretório caso não exista
  os.makedirs(DATASET_DIR, exist_ok=True)

  for i in range(1 , 13):
   nome_arquivo = os.path.join(DATASET_DIR, f'VRA_2024_{i:02d}.csv')

   ## Verifica se o arquivo já existe
   if verificar_arquivo_existe(nome_arquivo):
        print(f"Arquivo já existe: {nome_arquivo}. Pulando download.")
        continue
   
   
   baixar_arquivo(BASE_URL.format(i), nome_arquivo)


# Carregando os arquivos



# Armazenando os dados

