x=0
c=0
soma=0
n=0
r=''
while r != 'N':
    x = int(input('Numero:'))
    soma=soma+x
    n=n+1
    r=input("Continuar:").upper()
    if r == 'N':
        print('Média é {}'.format(soma/n))