'''matriz = [[], [], []]

for linha in range(1, 4):
    for coluna in range(1, 4):
        entrada = int(input(f"Digite o elemento {linha},{coluna}: "))
        if linha == 1:
            matriz[0].append(entrada)
        elif linha == 2:
            matriz[1].append(entrada)
        else:
            matriz[2].append(entrada)

print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')'''
# Solução do guanabara:
matrix=[[0,0,0], [0,0,0], [0,0,0]]
for linha in range (3):
    for coluna in range (3):
        matrix[linha][coluna] = int(input(f'Valor para [{linha}, {coluna}]:'))

for linha in range(3):
    for coluna in range(3):
        print(f'[{matrix[linha][coluna]:^5}]', end='')
    print()
