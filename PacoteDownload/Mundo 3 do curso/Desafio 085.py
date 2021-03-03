lista = [[], []]
for i in range(7):
    entrada = int(input(f'Digite o {i+1}º Número: '))
    if entrada % 2 == 0:
        lista[0].append(entrada)
    else:
        lista[1].append(entrada)
'''
lista[0].sort()
lista[1].sort()
print(f'Lista dos Pares: {lista[0]}')
print(f'Lista dos Impares: {lista[1]}')'''

# Posso utilizar alternativamente:
print(f'Lista dos pares: {sorted(lista[0])}')
print(f'Lista dos impares: {sorted(lista[1])}')
