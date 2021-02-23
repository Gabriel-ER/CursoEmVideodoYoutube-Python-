lista = []
pares = []
impares = []
while True:
    r = input("Enter para continuar: ").upper().strip()
    if r == '':
        lista.append(int(input("Número: ")))
    else:
        for i in lista:
            if i % 2 == 0:
                pares.append(i)
            else:
                impares.append(i)
        print(f'Pares: {pares}')
        print(f'Impares: {impares}')
        break