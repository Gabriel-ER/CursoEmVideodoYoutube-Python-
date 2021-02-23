a = []
maior = 0
menor = 0
for i in range(5):
    novo = int(input("Digite o número: "))
    if len(a) == 0:
        a.append(novo)
        maior=menor=novo
        print(f'Lista:{a}')
    else:
        for k in range(len(a)):
            if novo > a[k]:
                a.insert(novo, a[k])
                print(f'{k}: Lista: {a}')
    '''else:
        for elemento in a:
            if j >= a[elemento]:
                a.insert(j, a[elemento])
                print(a)
            else:
                a.insert(j, (a[elemento] - 1))'''
