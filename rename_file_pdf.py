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

    def delete_file(self, ):
        if(os.path.exists(r'C:\Users\Warley Souza\Music\read_excel\pdf_file\name.txt')):
                os.remove(r'C:\Users\Warley Souza\Music\read_excel\pdf_file\name.txt')
    
    def create_file(self, ):
        os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf_file")
        os.listdir()

        for name in os.listdir():
                 
            with pdfplumber.open(name) as temp:
                    first_page = temp.pages[0]
                    lista = first_page.extract_text()
                    file = lista

                    with open('name.txt', 'w') as arquivo:
                        arquivo.write(str(lista)+ '\n')
                        break

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
                    # Esse for abaixo aqui é só para tirar o "\n" em algumas strings, é opcional.
                    for i in texto:
                        local = texto.index(i) # Local do i em texto
                        for b in i:
                            local2 = texto[local].index(b) # Local2 do b em i ( local )
                            if "\n" in b:
                                texto[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"


                    index_list = texto

                    #transforma cada linha do arquivo txt em um index pra lista
                    for i, frase in enumerate(index_list):
                        index_list[i] = frase[0].split()
                        if index_list[i][0] == 'Location:':
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
                            break
                        else:
                            pass
                    for item in index_list:
                        try:                   
                            #transforma o primeiro item do index em um inteiro
                            index = int(item[0][0])
                            if index <= 1000:
                                test_age = item[8]
                                cube = item[1]
                                break
                        except:
                            pass
            name_file = name
            f.close()
            try:
                # os.chdir(r"C:\Users\Warley Souza\Music\read_excel\New folder")
                os.chdir(r"C:\Users\Warley Souza\Glenbrier Ltd\Projects - NX-Site Master\xx NX - Design Team xx\09 - BCAR\04 - Concrete Cubes\01 - Results")
                os.listdir()
                cont = len(os.listdir())+1
                teste = (f'{cont} - {floor} {tipo} - ({cube}) - {test_age} Days')
                # os.rename(r'C:\Users\Warley Souza\Music\read_excel\pdf_file\{}'.format(name_file),
                #         r'C:\Users\Warley Souza\Music\read_excel\New folder\{}.pdf'.format(teste))
                os.rename(r'C:\Users\Warley Souza\Music\read_excel\pdf_file\{}'.format(name_file),
                          r'C:\Users\Warley Souza\Glenbrier Ltd\Projects - NX-Site Master\xx NX - Design Team xx\09 - BCAR\04 - Concrete Cubes\01 - Results\{}.pdf'.format(teste))
            except:
                print("Sem arquivos para mover!")
            
            # 
            # 
                


# test = Name_PDF().name_pdf()
# create = Name_PDF().create_file()