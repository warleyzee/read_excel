from csv import excel
import pandas as pd

excel = pd.read_excel(r"C:\Users\Warley Souza\Music\read_excel\test.xlsx", engine='openpyxl')
excel.head()
print(excel)



dados = {'Compressive': '38.4',       
        'Cube Ref': '1A',
        'Date of Test': '09/02/2022',
        'Density': '2340',
        'Teste Age': '9'
        }

# print(dados['Cube Ref'])

dados_filtrados = excel['Cube'] == dados['Cube Ref']

print(excel[dados_filtrados])