pessoas = list()
lista_aux = list()
pesos = []
maiores = []
menores = []
while True:
    lista_aux.append(str(input("Nome: ")))
    lista_aux.append((float(input("Peso: "))))
    pessoas.append(lista_aux[:])
    lista_aux.clear()
    continar = input("Continuar? [S/N]")
    if continar in 'NnNão':
        break
print(f'{pessoas}')
for p in pessoas:
    pesos.append(p[1])
print(f'Total de pessoas: {len(pessoas)}')
'''Esse foi o peso de {pessoas[pesos.index(max(pesos))][0]}
print(f'O menor peso foi de {min(pesos)}. Esse foi o peso de {pessoas[pesos.index(min(pesos))][0]}')'''

print(f'O maior peso foi {max(pesos)}. Esse é o peso de', end=' ')
for p in pessoas:
    if p[1] == max(pesos):
        print(f'{p[0]} ...', end=' ')
print()
print(f' O menor peso foi {min(pesos)}. Esse é o peso de ', end= ' ')
for p in pessoas:
    if p[1] == min(pesos):
        print(f'{p[0]} ...', end=' ')
