def sorteia():
    from random import randint
    sorteados = []
    for i in range(5):
        sorteados.append(randint(1,10))
    # print(sorteados)
    return (sorteados)
def somapar(x):
    soma = 0
    print(f'sorteados: {x}')
    for i in x:
        if i%2 == 0:
            soma += i
    print(soma)
    return (soma)

#sorteia()
#somapar([1,2,3,40])
somapar(sorteia())

