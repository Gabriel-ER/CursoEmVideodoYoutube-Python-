'''def tupla_aleatória():
    from random import randint
    from time import sleep
    minha_tupla=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
    #print(min(minha_tupla))
    #sleep(1)
    return minha_tupla

contador_de_tuplas = 1
contade_da_escolhida = 0
#Uma: 64997, 167923, 27585, 115355, 83546
#Três: 553016, 224102, 122229, 752989
#Dez:1777489, 1435427
#100: 14789115
while True:
    tupla_aleatória()
    contador_de_tuplas += 1
    if tupla_aleatória() == (9,9,9,9,9):
        contade_da_escolhida += 1
        if contade_da_escolhida == 10:
            print(f'Saiu em {contador_de_tuplas}')
            break
'''
'''num = [1,2,3,4]
print(num)
num[2]=255
print(num)
num.append(7) #modifica minha lista e reatribui à variável
num.sort()
print(num)
num.sort(reverse=True)
num.insert(2,1299)
print(num)
num.pop()
print(num)
num.pop(1)
print(num)
num.remove(1299)
print(num)'''

from random import randint
valores = []
for i in range(5):
    valores.append(randint(1,10))
print(valores)

for c, v in enumerate(valores):
    print(f'O valor {v} está na posição {c}')
    print(list(enumerate(valores)))

#Observação importante: Para copiar uma lista,
# devo usar b=a[:]
#Se usar b=a, as duas listas ficam ligadas e o que eu fizer em uma
#acontece na outra
