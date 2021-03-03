from random import randint
jogo = []
qtd_jogos = int(input("Quantos jogos? "))
for i in range(qtd_jogos):
    for k  in range(6):
        jogo.append(randint(1,60))

    print(sorted(jogo))
    jogo.clear()