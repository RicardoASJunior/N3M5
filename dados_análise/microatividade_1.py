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

    def display_data(self):
        if self.data is not None:
            print(self.data)
        else:
            print("Nenhum dado disponível para exibir.")

if __name__ == "__main__":
    
    reader = DataReader('csv/Online Retail.csv')
    
    reader.read_excel()
    
    reader.display_data()
