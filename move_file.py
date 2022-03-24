import os
import shutil

"""
    Classe responsavel por mudar os arquivos word da raiz do projeto para a pasta ContratosWORD
"""
class MoveFile():

    def move_file(self,):
        try:
            #caminho de onde o arquivo  original se encontra
            os.chdir(r"C:\Users\Warley Souza\Music\read_excel")
            

            os.listdir()
            """
                for para percorrer a pasta do caminho onde se encontra todos os arquivos do projeto 
                se encotrar algum arquivo com o nomem 'Contrato_' move para a pasta ContratoWORD
            """
            for file in os.listdir():
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


# teste = MoveFile()
# teste.move_file_xlsx()
