from random import randint

numero = randint(0, 1)
palpite=int(input('palpite:'))
tentativas=1
if palpite == numero:
    print("acertou mizeravi! Com uma tentativa")
else:
   print('errou')