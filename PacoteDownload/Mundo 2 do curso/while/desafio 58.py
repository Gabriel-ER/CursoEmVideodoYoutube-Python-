from random import randint as numero_aleatorio
adivinhado = numero_aleatorio(1, 10)
print(adivinhado)
palpite = int(input("Digite seu palpite:"))
num_palpites = 1

while palpite != adivinhado:
    print('Errado')
    num_palpites+=1
    palpite = int(input("Digite o seu {}º palpite".format(num_palpites)))
print("Acertou no seu {}º palpite".format(num_palpites))