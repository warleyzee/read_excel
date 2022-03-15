import pandas as pd
from all_pdf import Read_PDF

class File_Excel():

    def save_file_exce(self,):

        dados = Read_PDF().create_list_pdf()

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
          
