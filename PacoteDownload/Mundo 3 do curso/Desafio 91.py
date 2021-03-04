from random import randint
from operator import itemgetter
#dados = {'a':2,'b':1,'c':10,'d':5}
dados={}
ranking = []
for i in range(4):
    dados[f'jogador {i+1}'] = randint(1,6)
print(dados)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True) #Se fosse 0 e não 1, seria por chave,
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')