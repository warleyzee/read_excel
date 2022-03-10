from pprint import pprint
import pdfplumber
with pdfplumber.open("test.pdf") as temp:
  first_page = temp.pages[0]
  lista = first_page.extract_text()

file = lista
with open('dados.txt', 'w') as arquivo:
  arquivo.write(str(file)+ '\n') 


f = open("dados.txt",'r')
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


lista2 = texto

for i, frase in enumerate(lista2):
  lista2[i] = frase[0].split()

colum = lista2[22] 

# print(lista2)
print("lista2 =",lista2[22])
dados = {
          "Cube Ref":colum[1],
          "Date of Test":colum[7],
          "Teste Age":colum[8],
          "Density":colum[10],
          "Compressive":colum[12]         
}

print()
pprint(dados)


  


