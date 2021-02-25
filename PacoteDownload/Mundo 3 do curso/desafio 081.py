lista = []

while True:
    resposta = input('Continuar? ')
    if resposta[0] in 'NnP':
        break
    else:
        lista.append(int(input("_:")))

lista.sort(reverse=True)

print(F"""A lista tem {len(lista)} valores, 
seus valores ordenados são: {lista}. """)
if 5 in lista:
    print('5 está na lista')
else:
    print('5 não está na lista')
