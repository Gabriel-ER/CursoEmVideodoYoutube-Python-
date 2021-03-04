'''dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
# dados['sexo'] = 'M'

print(dados)
print(dados['sexo'])

# del dados ['idade']

print(dados)

print(dados.values())
print(dados.keys())
print(dados.items())

for k, v in dados.items():
    print(f'O {k} é {v}')

alunos = [
    {'Nome': 'Gabriel', 'idade': 24, 'sexo': 'M'},
    {'Nome': 'Nathalia', 'idade': 23, 'sexo': 'F'},
    {'Nome': 'Santos', 'idade': 31, 'sexo': 'F'}]
print(alunos[0]['idade'])
print(type(alunos[0]))
# alunos={'a','b'}
# print(type(alunos))

for aluno in alunos:
    print(aluno.values())
dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
print('====Chaves====')
for key in dados.keys():
    print(key)
print('====Valores====')
for valor in dados.values():
    print(valor)
print('====Items====')
for item in dados.items():
    print(item)'''

'''brasil = []
estado1 = {'uf': 'Rio', 'sigla':'RJ'}
estado2 = {'uf': 'Dist Fed', 'sigla':'DF'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)'''

estado = dict()
brasil = list()
for c in range (3):
    estado['uf'] = str(input('Unidade da Federação: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

'''for estado in brasil:
    # print(estado)
    for k, v in estado.items():
        print(f'O campo {k} tem valor {v}')
'''
for e in brasil:
        for v in e.values():
            print(v, end=' ')
        print()
print(brasil)
