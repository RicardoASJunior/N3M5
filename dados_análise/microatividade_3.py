import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self, nrows=10):
        """Carrega apenas as primeiras 'nrows' linhas do arquivo Excel."""
        try:
            self.data = pd.read_excel(self.file_path, nrows=nrows)
            print(f"Arquivo {self.file_path} carregado com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")

    def display_data(self):
        """Exibe o DataFrame carregado no console usando to_string."""
        if self.data is not None:
            print(f"Exibindo as primeiras {len(self.data)} linhas:")
            # Usando to_string para exibir como string
            print(self.data.to_string())
        else:
            print("Nenhum dado foi carregado. Use o método 'load_data()' primeiro.")

if __name__ == "__main__":
    # Criando uma instância da classe
    file_path = 'csv/Online Retail.csv'  # Verifique se o caminho está correto
    data_handler = DataHandler(file_path)

    # Carregando apenas as primeiras 10 linhas
    data_handler.load_data(nrows=10)

    # Exibindo os dados usando to_string()
    data_handler.display_data()
