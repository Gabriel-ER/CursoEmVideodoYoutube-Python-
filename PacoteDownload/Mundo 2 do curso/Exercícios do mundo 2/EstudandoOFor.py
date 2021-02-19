numero = int(input("Numero:\n"))
numero2 = numero-0
for i in range(numero, 0, -1):
    print(i,'-')
    for j in range(0, numero2):
        print(j)
    numero2 = numero2 - 1
