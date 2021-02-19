"""
from time import sleep as espera

x=10
k = 0
while k<x:
    print(k)
    k+=1
    espera(0.5)
print("fim")

"""

"""Defini uma função chamada contador. Ela pega um
argumento chamado tempo e guarda ele somado a um em uma
variável chamada x. O +1 é para o contador ir até o número final.
A espera de 0.5 segudndos é para o programa ir mais rápido."""

"""
def contador(tempo):
    from time import sleep as espera

    x = tempo + 1
    k = 0
    while k < x:
        print(k)
        k += 1
        espera(0.5)

    print("fim")
    return 0


# Fim da minha função contador.


tempo_usado_pelo_contador = int(input("Digite o tempo:\n"))
contador(tempo_usado_pelo_contador)
"""

#Usando uma condição de parada
"""
n = 1
while n != 0:
    n = int(input("Valor:\n"))
print("FIM")
"""
"""
r = 'S'
n = 0
soma=0
while r == 'S':
    n = int(input("Valor:"))
    r = str((input("Continuar? [S/N]\n"))).upper()
    soma=soma+n
print('A soma é {}'.format(soma))
print("FIM")
"""

#Imprimindo Infinitamente
"""n=1
k=0
while n>0:
    print(k)
    k+=1"""

