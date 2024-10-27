import pandas as pd

class DataReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_excel(self):
        try:
            self.data = pd.read_excel(self.file_path, engine='openpyxl')
            print("Dados lidos com sucesso!")
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    # Cria um subconjunto dos dados com as colunas especificadas
    def create_subset(self, columns):
        return self.data[columns]

    def display_data(self, data):
        if data is not None:
            print(data)
        else:
            print("Nenhum dado disponível para exibir.")

if __name__ == "__main__":
    reader = DataReader('csv/Online Retail.csv')
    reader.read_excel()
    
    subset_columns = ['InvoiceNo', 'StockCode', 'Description']
    subset_data = reader.create_subset(subset_columns)
    
    reader.display_data(subset_data)
