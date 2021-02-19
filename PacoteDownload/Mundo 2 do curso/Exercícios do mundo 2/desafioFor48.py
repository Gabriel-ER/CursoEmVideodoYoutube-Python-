soma = 0
for i in range(3, 501, 3):
    if i % 2 != 0:
        print(i)
        soma = soma+i
print(soma,'...')