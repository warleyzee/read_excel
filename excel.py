import pandas as pd
from pandas import Timestamp
from datetime import datetime
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side, PatternFill
from read_save_pdf import Read_Save_PDF

class File_Excel():

    def save_file_excel(self,):
        dados = Read_Save_PDF().create_list_pdf()
        table = pd.read_excel("Cube_finish.xlsx")
        survey_df = pd.DataFrame(table)
        days = ''
        result = ''
       
        for i in dados:

            date_of_test =  pd.to_datetime(i['Date of Test'], format='%d/%m/%Y')

            date_of_tested   =  pd.to_datetime(i['Date of Tested'], format='%d/%m/%Y')

            if i['Test Age'] == '7':
                result = i['Compressive Strength']
                days = '7 Day Result'
            elif i['Test Age'] == '14':
                result = i['Compressive Strength']
                days = '14 Day Result'
            elif i['Test Age'] == '28':
                result = i['Compressive Strength']
                days = '28 Day Result'
            elif i['Test Age'] == '56':
                result = i['Compressive Strength']
                days = '56 Day Result'
            else:
                result = i['Compressive Strength']+ '(' + i['Test Age'] + 'Days' + ')'
                days = '7 Day Result'
                pass

            table.loc[len(table), ['Cube','Date Cast','Location','Date Tested','Density', days]] = i['Client Ref'], date_of_test,i['Location'],date_of_tested,i['Density'],result
            table.to_excel("test.xlsx", index=False)

        print('Data Frame is written to Excel File Sucessfully')

# test = File_Excel().save_file_excel()          
