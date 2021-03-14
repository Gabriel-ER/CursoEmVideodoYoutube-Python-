def leiaint(a=''):
    while True:
        n = input(a)
        if n.isnumeric():
            n = int(n)
            print(f'Você digitou {n}')
            return n
            break
        else:
            print('\033[0;31m NO \033[m', end='\n')

leiaint('Digite um número: ')

