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
    
    def display_data_info(self):
        """Exibe informações gerais sobre as colunas, linhas e dados do DataFrame."""
        if self.data is not None:
            print("Informações gerais sobre o conjunto de dados:")
            self.data.info()
        else:
            print("Nenhum dado foi carregado. Use o método 'load_data()' primeiro.")
    
    def get_data_statistics(self):
        """Obtém estatísticas gerais sobre o conjunto de dados."""
        if self.data is not None:
            total_rows = self.data.shape[0]
            total_columns = self.data.shape[1]
            null_values = self.data.isnull().sum().sum()  # Soma todos os valores nulos
            memory_usage = self.data.memory_usage(deep=True).sum()  # Uso de memória
            
            print(f"Total de linhas: {total_rows}")
            print(f"Total de colunas: {total_columns}")
            print(f"Quantidade de dados nulos: {null_values}")
            print(f"Uso de memória (em bytes): {memory_usage}")
        else:
            print("Nenhum dado foi carregado. Use o método 'load_data()' primeiro.")

if __name__ == "__main__":
    # Criando uma instância da classe
    file_path = 'csv/Online Retail.csv'
    data_handler = DataHandler(file_path)

    # Carregando todos os dados
    data_handler.load_data()

    # Exibindo as informações gerais sobre o conjunto de dados
    data_handler.display_data_info()

    # Exibindo estatísticas como total de linhas, colunas, dados nulos e memória utilizada
    data_handler.get_data_statistics()
