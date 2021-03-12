total_gols = 0
gols = []
jogador = {}
jogador['Nome'] =input('Nome: ')
print(jogador)
qtd_jogos = int(input('Quantidade de jogos: '))
jogador['Numero de jogos'] = qtd_jogos
for i in range(qtd_jogos):
    gols.append(int(input(f'Gols na partida {i+1}: ')))
    total_gols += gols[i]
jogador['Gols'] = gols[:]
jogador['Numero de gols'] = total_gols
print(jogador)

print('-='*20)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Numero de jogos"]} partida(s)')
contador = 1
for j in jogador['Gols']:
    print(f'Na partida {contador}, fez {j} gols ')
    contador += 1
print(f'Foi um total de {qtd_jogos} jogados e {total_gols} feitos')