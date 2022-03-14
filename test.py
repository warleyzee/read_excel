from csv import excel
from msilib.schema import Error
from re import S
from tkinter import E
from numpy import tri
import pandas as pd

dados = [{'Client Ref': '1D',
  'Compressive Strength': '52.7',
  'Date of Test': '09/03/2022',  
  'Density': '2390',
  'Test Age': '6'},
 {'Client Ref': '1A',
  'Compressive Strength': '52.7',
  'Date of Test': '10/03/2022',  
  'Density': '2360',
  'Test Age': '56'},
 {'Client Ref': '1B',
  'Compressive Strength': '51.0',
  'Date of Test': '09/03/2022',  
  'Density': '2400',
  'Test Age': '28'},
 {'Client Ref': '1C',
  'Compressive Strength': '50.1',
  'Date of Test': '09/03/2022',  
  'Density': '2430',
  'Test Age': '28'},
 {'Client Ref': '1E',
  'Compressive Strength': '45.5',
  'Date of Test': '10/03/2022',
  'Density': '2380',
  'Test Age': '28'},
 {'Client Ref': '1F',
  'Compressive Strength': '39.3',
  'Date of Test': '10/03/2022',
  'Density': '2380',
  'Test Age': '28'},
 {'Client Ref': '95A',
  'Compressive Strength': '42.6',
  'Date of Test': '09/03/2022',
  'Density': '2360',
  'Test Age': '22'},
 {'Client Ref': '96A',
  'Compressive Strength': '41.2',
  'Date of Test': '09/03/2022',
  'Density': '2380',
  'Test Age': '21'},
 {'Client Ref': '97A',
  'Compressive Strength': '41.9',
  'Date of Test': '09/03/2022',
  'Density': '2380',
  'Test Age': '20'},
 {'Client Ref': '98A',
  'Compressive Strength': '46.5',
  'Date of Test': '09/03/2022',
  'Density': '2380',
  'Test Age': '19'},
 {'Client Ref': '106A',
  'Compressive Strength': '29.1',
  'Date of Test': '09/03/2022',
  'Density': '2370',
  'Test Age': '9'},
 {'Client Ref': '105A',
  'Compressive Strength': '30.2',
  'Date of Test': '09/03/2022',
  'Density': '2350',
  'Test Age': '9'},
 {'Client Ref': '103A',
  'Compressive Strength': '33.9',
  'Date of Test': '09/03/2022',
  'Density': '2350',
  'Test Age': '13'},
 {'Client Ref': '108A',
  'Compressive Strength': '31.1',
  'Date of Test': '09/03/2022',
  'Density': '2350',
  'Test Age': '7'},
 {'Client Ref': '107A',
  'Compressive Strength': '29.4',
  'Date of Test': '09/03/2022',
  'Density': '2360',
  'Test Age': '8'},
 {'Client Ref': '109A',
  'Compressive Strength': '25.8',
  'Date of Test': '10/03/2022',
  'Density': '2360',
  'Test Age': '7'},
 {'Client Ref': '99A',
  'Compressive Strength': '36.8',
  'Date of Test': '09/03/2022',
  'Density': '2370',
  'Test Age': '16'},
 {'Client Ref': '100A',
  'Compressive Strength': '37.3',
  'Date of Test': '09/03/2022',
  'Density': '2310',
  'Test Age': '15'},
 {'Client Ref': '101A',
  'Compressive Strength': '35.9',
  'Date of Test': '09/03/2022',
  'Density': '2400',
  'Test Age': '15'},
 {'Client Ref': '102A',
  'Compressive Strength': '36.9',
  'Date of Test': '09/03/2022',
  'Density': '2370',
  'Test Age': '14'}]

df = pd.read_excel(r"C:\Users\Warley Souza\Music\read_excel\test.xlsx", engine='openpyxl')
# df['Date Cast'].astype('datetime64')
df['Date Cast'] = df['Date Cast'].dt.strftime('%d/%m/%Y')


# print(df['Date Cast'])
survey_df = pd.DataFrame(df)
# survey_df.info()
# input()



for i in dados:
    for item, trial in survey_df.iterrows():
        cube = survey_df['Cube'] == i['Client Ref']
        survey_df.loc[cube,'Date Tested'] = i['Date of Test']
        survey_df.loc[cube,'Density'] = i['Density']
        if i['Test Age'] == '7':
            survey_df.loc[cube,'7 Day Result'] = i['Compressive Strength']
        elif i['Test Age'] == '14':
            survey_df.loc[cube,'14 Day Result'] = i['Compressive Strength']
        elif i['Test Age'] == '28':
            survey_df.loc[cube,'28 Day Result'] = i['Compressive Strength']
        elif i['Test Age'] == '56':
            #print( i['Test Age'])
            survey_df.loc[cube,'56 Day Result'] = i['Compressive Strength']
        else:
            survey_df.loc[cube,'7 Day Result'] = i['Compressive Strength']+ '(' + i['Test Age'] + 'Days' + ')'
            pass
        survey_df
        # input()
try:
    print()
    # df['Date Tested'] = df['Date Tested'].dt.strftime('%d/%m/%Y')
    file_name = ('Cube_finish.xlsx')
    survey_df.to_excel(file_name)
    print('Data Frame is written to Excel File Sucessfully')
except:
    print()
    print("Error")
print(survey_df)   
