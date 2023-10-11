from pprint import pprint
import os
import pdfplumber


class Read_Save_PDF():

    def save_pdf_txt(self, ):
        #Open the local the file pdf
        os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf_file")
        os.listdir()
        salve_pdf = []

        if len(os.listdir()) <= 0:
            print("Without file PDF from folder")
            print("The end...")
            input("Press enter to continue...")
        else:
            # For to get all PDF file
            for pdf in os.listdir():
                str_pdf = pdf[-3:]
                img = pdf[0:5]

                if img == "image":
                    pass
                    
                elif str_pdf == "pdf":
                    with pdfplumber.open(pdf) as temp:
                        first_page = temp.pages[0]
                        lista = first_page.extract_text()

                    # If the file same PDF, save he in a txt file
                    if(os.path.exists(r"C:\Users\Warley Souza\Music\read_excel\pdf_file\dados.txt")):
                        #opening file for be edit 
                        arquivo = open('dados.txt', 'r') 
                        salve_pdf.append(lista)
                        #Editing txt file with new pdf
                        arquivo = open('dados.txt', 'w')
                        arquivo.writelines(salve_pdf)
                        # close file after insert new pdf
                        arquivo.close()

                    else:
                        file = lista
                        with open('dados.txt', 'w') as arquivo:
                            arquivo.write(str(file)+ '\n') 
    
    def create_list_pdf(self,):

        self.item_excel = []
        
        #read file with all saved data
        f = open(r"C:\Users\Warley Souza\Music\read_excel\pdf_file\dados.txt", 'r')
        texto = f.readlines()

        x = 0

        while x < len(texto):
            if texto[x] == "\n":
                local = texto.index(texto[x])
                texto.pop(local)
            else:
                texto[x] = texto[x].split(',')
                x += 1
        #this for below is just to delete "\n" some strings
        for i in texto:
            local = texto.index(i) 
            for b in i:
                local2 = texto[local].index(b) 
                if "\n" in b:
                    texto[local][local2] = b.replace("\n",'')


        index_list = texto
        location = []
        location = "Location:"

        #transform each line from file txt in a index to list
        for i, frase in enumerate(index_list):
            index_list[i] = frase[0].split()

        for item in index_list:
            if location not in item:
                pass
            else:
                a = item
                # print (f'Esse index tem a chave {a}')
                del a[0]
                loc = ' '.join(a)
                # print(f'Resultado final e: {loc}')
                # input("TEST")
            
            try:
                #transform the first item index in a integer, 
                index = int(item[0][0])
                if index <= 1000:
                    self.item_excel.append({
                    'Client Ref': item[1],
                    'Date of Test': item[6],
                    'Date of Tested':item[7],
                    'Test Age':item[8],
                    'Density':item[10],
                    'Compressive Strength':item[12],
                    'Location': loc, 
                    })
            except:
                pass

        return (self.item_excel)

# test = Read_Save_PDF().save_pdf_txt() 
# test = Read_Save_PDF().create_list_pdf()
# print(test)








