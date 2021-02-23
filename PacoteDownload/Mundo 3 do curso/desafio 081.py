lista = []
resposta = ' '
while True:
    resposta = input('Continuar? ')
    if (resposta[0] in 'NnP'):
        break
    else:
        lista.append(int(input("_:")))

print(F"""A lista tem {len(lista)} valores, 
seus valores ordenados são: {lista[::-1]}. """)
if 5 in lista:
    print('5 eestá na lista')
else:
    print('5 não está na lista')
