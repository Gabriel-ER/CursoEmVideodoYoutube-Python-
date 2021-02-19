nome = []
preco = []
add_nome = ['']
add_preco = [0]
i = 0
total = 0
continuar = 'SsYYDdCc '
maiores_que_mil = 0
while True:
    resp_continue = input("Deseja continuar?")[0]
    if resp_continue in continuar:
        nome += add_nome
        preco += add_preco
        nome[i] = input("Digite o nome do produto: ")
        preco[i] = int(input("Digite o valor: "))
        if preco[i] > 1000:
            maiores_que_mil += 1
        print(f'{nome} : R${preco}')
        total = total + preco[i]
        i += 1
    else:
        print(f'O total é: {total}')
        print(f'Há {maiores_que_mil} maiores que mil.')
        print(f'O menor valor foi {min(preco)} para o item {nome[preco.index(min(preco))]}')
        break
