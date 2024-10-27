import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        """Carrega o conjunto de dados completo do arquivo Excel."""
        try:
            self.data = pd.read_excel(self.file_path)
            print(f"Arquivo {self.file_path} carregado com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")
    
    def display_first_n_rows(self, n=10):
        """Exibe as primeiras 'n' linhas do DataFrame."""
        if self.data is not None:
            print(f"Exibindo as primeiras {n} linhas:")
            print(self.data.head(n).to_string())
        else:
            print("Nenhum dado foi carregado. Use o método 'load_data()' primeiro.")
    
    def display_last_n_rows(self, n=10):
        """Exibe as últimas 'n' linhas do DataFrame."""
        if self.data is not None:
            print(f"Exibindo as últimas {n} linhas:")
            print(self.data.tail(n).to_string())
        else:
            print("Nenhum dado foi carregado. Use o método 'load_data()' primeiro.")

if __name__ == "__main__":
    # Criando uma instância da classe
    file_path = 'csv/Online Retail.csv'  # Verifique se o caminho está correto
    data_handler = DataHandler(file_path)
    
    # Carregando todos os dados
    data_handler.load_data()
    
    # Exibindo as primeiras 10 linhas
    data_handler.display_first_n_rows(n=10)
    
    # Exibindo as últimas 10 linhas
    data_handler.display_last_n_rows(n=10)
