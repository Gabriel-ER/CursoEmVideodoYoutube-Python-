matriz = [[], [], []]

for l in range (1,4):
    for c in range(1,4):
        entrada = int(input(f"Digite o elemento {l},{c}: "))
        if l == 1:
            matriz[0].append(entrada)
        elif l == 2:
            matriz[1].append(entrada)
        else:
            matriz[2].append(entrada)
print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')




'''for i in range(9):
    entrada = int(input(f"Digite o elemento {l},{c}: "))
    c += 1
    if i < 3:
        matriz[0].append(entrada)
    elif i >= 3 and i < 6:
        matriz[1].append(entrada)
    else:
        matriz[2].append(entrada)
print(matriz)'''