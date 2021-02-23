a = []

for i in range(5):
    a.append(int(input(f'{i}:')))

print(f'A lista a: {a}')

maior_valor = max(a)
menor_valor = min(a)
posicoes_minimas = [a.index(min(a))]
posicoes_maximas = [a.index(max(a))]

cont_minimos = a.count(a[a.index(min(a))])
print(f'O minimo aparece {cont_minimos} vezes e é {menor_valor}. Posições:', end='')
for i, v in enumerate(a):
    if a[i] == menor_valor:
        print(f', {i} ', end='')

print('\n')

cont_maximos = a.count(a[a.index(max(a))])
print(f'O maximo aparece {cont_maximos} vezes e é {maior_valor}. Posições:', end='')
for i, v in enumerate(a):
    if a[i] == maior_valor:
        print(f', {i} ', end='')

print('\n')
