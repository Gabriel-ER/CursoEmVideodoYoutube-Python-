from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somaimpares = soma_terceira = 0

'''for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite o valor [{linha},{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]'''
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = randint(0, 50)
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]

contador = 0
while contador < 3:
    soma_terceira += matriz[contador][2]
    contador += 1

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna] :^5}]', end='')
    print()
print(f'A soma da terceira coluna é: {soma_terceira}')
print(f'O máximo da segunda linha é {max(matriz[1])}')
print(f'A soma dos pares é: {somapares}')
