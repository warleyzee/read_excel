import os
from pprint import pprint 
import pdfplumber
"""

"""  

class Name_PDF():

    def name_pdf(self, ):
        self.name_pdf = []
        os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf_file")
        os.listdir()
        
        for name in os.listdir():
            str_pdf = name[-3:]

            if str_pdf == 'pdf':
                
                with pdfplumber.open(name) as temp:
                        first_page = temp.pages[0]
                        lista = first_page.extract_text()

                        file = lista
                        with  open('name.txt', 'w') as arquivo:
                            arquivo.write(str(lista)+ '\n')

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
                            for item in index_list:
                                print(item)
                                input()
                                if len(self.name_pdf) < 0:
                                    print(len(self.name_pdf))
                                    if item[0] == 'Location:':
                                        self.name_pdf.append({
                                            'Location': item[0],
                                            'Flor' : item[1],
                                            'type': item[2],
                                        })
                                else:
                                    pass
                            

        print("FIM")
        print(self.name_pdf)
        input("FIMFIM")


test = Name_PDF().name_pdf()