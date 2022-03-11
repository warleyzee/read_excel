from csv import excel
from tkinter import E
import pandas as pd

excel = pd.read_excel(r"C:\Users\Warley Souza\Music\read_excel\test.xlsx", engine='openpyxl')
# excel.head()
excel.info()
# dados = excel.to_excel("Nome do arquivo")



dados = {'Compressive': '38.4',       
        'Cube Ref': '1G',
        'Date of Test': '09/02/2022',
        'Density': '2340',
        'Teste Age': '9'
        }

# print(dados['Cube Ref'])

dados_filtrados = excel['Cube'] == dados['Cube Ref']


print(excel[dados_filtrados])