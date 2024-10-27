import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.modified_data = None

    def load_data(self):
        #Carrega o conjunto de dados CSV.
        try:
            self.data = pd.read_csv(self.file_path, sep=';', engine='python', encoding='utf-8')
            print("Dados carregados com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar os dados: {e}")
    
    def display_info(self):
        #Exibe informações gerais do conjunto de dados.
        if self.data is not None:
            print("Informações gerais do conjunto de dados:")
            self.data.info()
        else:
            print("Dados não carregados.")

    def display_head_and_tail(self, n=10):
        #Exibe as primeiras e últimas N linhas do conjunto de dados.
        if self.data is not None:
            print(f"As primeiras {n} linhas do conjunto de dados:")
            print(self.data.head(n).to_string())
            print(f"\nAs últimas {n} linhas do conjunto de dados:")
            print(self.data.tail(n).to_string())
        else:
            print("Dados não carregados.")

    def create_copy_and_modify(self):
        #Cria uma cópia dos dados e faz modificações como tratamento de valores nulos.
        if self.data is not None:
            # Criando uma cópia dos dados
            self.modified_data = self.data.copy()
            
            # Substituindo valores nulos da coluna 'Calories' por 0
            self.modified_data['Calories'].fillna(0, inplace=True)
            print("Valores nulos da coluna 'Calories' substituídos por 0.")
            
            # Substituindo valores nulos da coluna 'Date' por '1900/01/01'
            self.modified_data['Date'].fillna('1900/01/01', inplace=True)
            print("Valores nulos da coluna 'Date' substituídos por '1900/01/01'.")
        else:
            print("Dados não carregados.")

    def convert_date_column(self):
        #Converte a coluna 'Date' para o formato datetime.
        if self.modified_data is not None:
            # Substituindo '1900/01/01' por NaN
            self.modified_data['Date'].replace('1900/01/01', np.nan, inplace=True)
            print("'1900/01/01' substituído por NaN.")

            # Tentativa de converter a coluna 'Date' para datetime (ainda com problemas)
            try:
                self.modified_data['Date'] = pd.to_datetime(self.modified_data['Date'], format='%Y/%m/%d', errors='raise')
            except Exception as e:
                print(f"Erro ao converter as datas: {e}")

            # Corrigindo o valor '20201226' para o formato correto
            self.modified_data['Date'] = self.modified_data['Date'].replace('20201226', '2020/12/26')
            
            # Tentativa de conversão final
            self.modified_data['Date'] = pd.to_datetime(self.modified_data['Date'], format='%Y/%m/%d', errors='coerce')
            print("Coluna 'Date' convertida com sucesso para datetime.")
        else:
            print("Nenhum dado foi modificado.")

    def drop_null_values(self):
        #Remove registros que possuem valores nulos.
        if self.modified_data is not None:
            # Removendo registros com valores nulos
            self.modified_data.dropna(inplace=True)
            print("Registros com valores nulos removidos.")
        else:
            print("Nenhum dado foi modificado.")

    def display_modified_data(self):
        #Exibe o conjunto de dados modificado.
        if self.modified_data is not None:
            print(self.modified_data.to_string())
        else:
            print("Nenhum dado foi modificado.")

if __name__ == "__main__":
    # Caminho do arquivo CSV
    file_path = 'csv/Online Retail.csv'

    # Instanciando a classe DataProcessor
    processor = DataProcessor(file_path)

    # Carregando os dados
    processor.load_data()

    # Exibindo as informações gerais do conjunto de dados
    processor.display_info()

    # Exibindo as primeiras e últimas 10 linhas
    processor.display_head_and_tail()

    # Criando cópia e modificando os dados
    processor.create_copy_and_modify()

    # Convertendo a coluna 'Date' para datetime
    processor.convert_date_column()

    # Removendo valores nulos
    processor.drop_null_values()

    # Exibindo o conjunto de dados modificado
    processor.display_modified_data()