from pprint import pprint
import os
import pdfplumber


#Abrir local do arquivo.
os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf")
os.listdir()
salve_pdf = []
item_excel = []
i = 0
# For para pegar todo os dados que sao tipo PDF
for pdf in os.listdir():
    str_pdf = pdf[-3:]

    if str_pdf == "pdf":

        with pdfplumber.open(pdf) as temp:
            first_page = temp.pages[0]
            lista = first_page.extract_text()

        #Se o arquivo for PDF salva ele em um arquivo txt
        if(os.path.exists(r"C:\Users\Warley Souza\Music\read_excel\pdf\dados.txt")):
            #Abrir arquivo para ser editado
            arquivo = open('dados.txt', 'r') 
            salve_pdf.append(lista)

            #Editar arquivo txt com novo pdf
            arquivo = open('dados.txt', 'w')
            arquivo.writelines(salve_pdf)
            #fechar arquivo apos inserir novo pdf
            arquivo.close()

        else:
            #Se o arquivo nao existir criar ele primeiro
            file = lista
            with open('dados.txt', 'w') as arquivo:
                arquivo.write(str(file)+ '\n') 

#ler o arquivo com todo os arquivos pdf salvo
f = open('dados.txt', 'r')
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

#for para percorrer a lista
for item in index_list:
    try:
        #transforma o primeiro item do index em um inteiro
        index = int(item[0][0])
        if index <= 1000:
            item_excel.append({
               'Client Ref': item[1],
               'Date of Test':item[7],
               'Test Age':item[8],
               'Density':item[10],
               'Compressive Strength':item[12], 
            })
            
    except:
        pass

pprint(item_excel)






