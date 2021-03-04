from random import randint
from time import sleep
jogo = []
qtd_jogos = int(input("Quantos jogos? "))
for i in range(qtd_jogos):

    for k in range(6):
        novo = randint(1,60)
        
        while novo in jogo:
            novo = randint(1,60)
        jogo.append(novo)
    print(sorted(jogo))
    jogo.clear()
    sleep(0.5)