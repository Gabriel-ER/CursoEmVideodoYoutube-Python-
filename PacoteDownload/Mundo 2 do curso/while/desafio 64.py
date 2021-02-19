x=int(input('digite seu número: '))
c=999
soma=0
n_entradas=0
while x!=999:
    if x != 999:
        soma = soma+x
        n_entradas += 1
        x = int(input('digite seu número: '))
print('A soma é {} e foram {} entradas.'.format(soma,n_entradas))