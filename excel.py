from csv import excel
from tkinter import E
import pandas as pd

excel = pd.read_excel(r"C:\Users\Warley Souza\Music\read_excel\test.xlsx", engine='openpyxl')
# excel.head()
# excel.info()
print(excel)