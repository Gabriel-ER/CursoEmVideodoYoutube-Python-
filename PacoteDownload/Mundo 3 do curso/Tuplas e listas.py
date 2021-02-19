def tupla_aleatória():
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
        if contade_da_escolhida == 100:
            print(f'Saiu em {contador_de_tuplas}')
            break


