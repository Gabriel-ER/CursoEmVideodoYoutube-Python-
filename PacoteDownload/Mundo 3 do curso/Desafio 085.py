#auxiliar = []
principal = []
pares = []
impares = []


for i in range (7):
    entrada = float(input(f"Número {i}: "))
    if entrada % 2 == 0:
        principal.append(entrada)
    else:
        principal.insert(0,entrada)

print(principal)



'''for i in range (7):
    entrada = float(input(f"Número {i}: "))
    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)

for par in pares:
    principal.append(par)
for impar in impares:
    principal.append(impar)


print(principal)'''