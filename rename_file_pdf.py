from ast import iter_child_nodes
from asyncio.base_futures import _FINISHED
import os
from pprint import pprint
from turtle import fd
from venv import create 
import pdfplumber
"""

"""  

class Name_PDF():

    #delete file with name "name"
    def delete_file(self, ):
        if(os.path.exists(r'C:\Users\Warley Souza\Music\read_excel\pdf_file\name.txt')):
                os.remove(r'C:\Users\Warley Souza\Music\read_excel\pdf_file\name.txt')
    
    #create file txt with name "name"
    def create_file(self, ):
        os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf_file")
        os.listdir()

        for name in os.listdir():
            print(name)
                 
            with pdfplumber.open(name) as temp:
                    first_page = temp.pages[0]
                    lista = first_page.extract_text()
                    file = lista

                    with open('name.txt', 'w') as arquivo:
                        arquivo.write(str(lista)+ '\n')
                        break

    #save fale in another folder with the rigth name
    def name_pdf(self, ):
        
        os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf_file")
        os.listdir()
        
        for name in os.listdir():
            delete = Name_PDF().delete_file()
            create = Name_PDF().create_file()

            str_pdf = name[-3:]
                
            f = open(r"C:\Users\Warley Souza\Music\read_excel\pdf_file\name.txt", 'r')
            texto = f.readlines()
            x = 0

            while x < len(texto):
                if texto[x] == "\n":
                    local = texto.index(texto[x])
                    texto.pop(local)
                else:
                    texto[x] = texto[x].split(',')
                    x += 1  
            if str_pdf == 'pdf':
                    for i in texto:
                        local = texto.index(i) 
                        for b in i:
                            local2 = texto[local].index(b) 
                            if "\n" in b:
                                texto[local][local2] = b.replace("\n",'') 


                    index_list = texto

                    #transform each line from file txt in a index to list
                    for i, frase in enumerate(index_list):
                        index_list[i] = frase[0].split()

                        if index_list[i][0] == 'Location:':
                            # print(index_list)
                            # input("NEXT")
                            floor = index_list[i][1]
                            tipo = index_list[i][2]
                            if floor == '1':
                                floor = '1st'
                            elif floor == 'first':
                                floor = '1st'
                            elif floor == '2':
                                floor = '2nd'
                            elif floor == 'Grd':
                                floor = 'Ground'
                            elif tipo == 'Flr':
                                tipo = 'Floor'
                            elif tipo == '':
                                tipo = 'Floor'
                            break
                        else:
                            pass
                    for item in index_list:
                        try:                   
                             #transform the first item index in a integer, 
                            index = int(item[0][0])
                            if index <= 1000:
                                test_age = item[8]
                                cube = item[1]
                                break
                        except:
                            pass
            name_file = name            
            #close the file at the end
            f.close()

            try:
                os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf_name")
                        #    C:\Users\Warley Souza\OneDrive - Glenbrier Ltd\NX-Site Master\xx NX - Design Team xx\09 - BCAR\04 - Concrete Cubes\01 - Results
                os.listdir()
                cont = len(os.listdir())+647
                #rename the file with, floor, tipo, cube, test_age
                teste = (f'{cont} - {floor} {tipo} - ({cube}) - {test_age} Days')

                os.rename(r'C:\Users\Warley Souza\Music\read_excel\pdf_file\{}'.format(name_file),
                          r'C:\Users\Warley Souza\Music\read_excel\pdf_name\{}.pdf'.format(teste))
            except:
                print("without file to move")

# test = Name_PDF().name_pdf()
# create = Name_PDF().create_file()