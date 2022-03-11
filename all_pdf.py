import os
import pdfplumber

os.chdir(r"C:\Users\Warley Souza\Music\read_excel\pdf")
os.listdir()
salve_pdf = []
i = 0
for pdf in os.listdir():
    str_pdf = pdf[-3:]

    if str_pdf == "pdf":

        with pdfplumber.open(pdf) as temp:
            first_page = temp.pages[0]
            lista = first_page.extract_text()
    
        if(os.path.exists(r"C:\Users\Warley Souza\Music\read_excel\pdf\dados.txt")):
            arquivo = open('dados.txt', 'r') 
            salve_pdf.append(lista)

            arquivo = open('dados.txt', 'w')
            arquivo.writelines(salve_pdf)

            arquivo.close()
        else:
            file = lista
            with open('dados.txt', 'w') as arquivo:
                arquivo.write(str(file)+ '\n') 

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

for i, frase in enumerate(index_list):
  index_list[i] = frase[0].split()

print(type(index_list[22][0]))

for i in index_list:
    print(i)






