# import json
# from pprint import pprint


# lista = [['1','as','','asdf','','asdfasdfa','asdffeew','','','',],
#         ['sd','sfsdfsf','','','asdf','',],
#         ['4','as','','asdf','','asdfasdfa','asdffeew','','','',],
#         ['gas',],
#         ['3','asdf','','dfa','','  asdf','',],
#         ['hasd','','asd','asdfas','','asdf',],
#         ['2','asdf','','','','',]]

# dados = []
# for item in lista:
#     i = int(item[0])
#     print(i)
#     if i == 1:
#         dados.append({'Compressive': item[0],       
#         'Cube Ref': item[1],
#         'Date of Test': item[3],
#         'Density': item[5],
#         'Teste Age': item[6]
#         })

#     else:
#         print('DEU ERRADO')
        

# pprint(dados)

m = [ 
        ['1','asd'],
        ['2','sag'],
        ['a','asd'],
        ['4','sag'],
        ['g','asd'],
        ['6','sag'],
        ['d','sag'],
        ['6000','sag'],
    ]

dados = []
cont = 0
for item in m:
    try:
        teste = int(item[0][0])
        print(teste)
        print(type(teste))
        if teste <= 1000:
            print('entrou')
            dados.append({
                'Numero':item[0],
                'String':item[1],
            })
            print(dados) 

        cont += 1 
    except:
        cont += 1 
        print(cont)
        pass
        
print(dados)
print(cont)




# i = int(m[0][0])


# print(type(i))
# print(m[0][0])