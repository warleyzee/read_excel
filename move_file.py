import os
import shutil

"""
    Classe responsavel por mudar os arquivos PDF da raiz do projeto para a pasta pdf_file
"""
class MoveFile():

    def move_file(self,):
        try:
            #original file location
            os.chdir(r"C:\Users\Warley Souza\Music\read_excel")

            os.listdir()

            #going through all files from folder
            for file in os.listdir():
                #take the last 3 character from file
                str_pdf = file[-3:]
                if str_pdf == "pdf":
                    os.rename(file, r"C:\Users\Warley Souza\Music\read_excel\pdf_file" + "\\" + file)
                            
        except:
            pass
            
        for file in os.listdir():
                str_pdf = file[-3:]
                if str_pdf == "pdf":
                    os.remove(file)
                else:
                    pass
    
    def move_file_xlsx(self, ):
        
        try:
            os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf_file")
            os.listdir()

            for file in os.listdir():
                excel = file[-4:]
                if excel == "xlsx":
                    os.rename(file, r"C:\Users\Warley Souza\Music\read_excel" + "\\" + file)
        except:
            print("File not found!!!")


# teste = MoveFile().move_file()
# teste = MoveFile().move_file_xlsx()
