def area():
    l = float(input('Largura: '))
    c = float(input('Comprimento: '))
    print(f'Área: {l * c}m2')


def bordas(msg):
    print('-' * (len(msg)+4))
    print(f'  {msg}')
    print('-' * (len(msg)+4))


def contador():
    from time import sleep

    opcao = input("""
    Opção: 
    A: Conta de 1 a 10 de 1 em 1  
    B: Conta de 10 a 0 de 1 em 1 
    C: Personalizada
     """).upper()
    # opcao = 'C' #Desmarque para o programa já começar na personalizada

    if opcao == 'A':

        for n in range(1, 11):
            print(n)
            sleep(0.3)

    if opcao == 'B':
        for n in range(10, -1, -2):
            print(n)
            sleep(0.3)

    if opcao == 'C':
        inicio = int(input('Início: '))
        fim = int(input('Fim: '))
        passo = int(input('Passo: '))
        if passo == 0:
            passo = 1

        if inicio > fim:
            if passo < 0:
                passo *= -1
            for n in range(inicio, fim - 1, -passo):
                print(n)
                sleep(0.3)
        for n in range(inicio, fim + 1, passo):
            print(n)
            sleep(0.3)
def maior(*num):

    print(max(num))



# Programa principal

programa_escolhido = input(
"""Digite o nome do programa: 
    -bordas
    -area
    -contador
    -maior
    --> 
""").lower().strip()
if programa_escolhido == 'bordas':
    bordas(input('Mensagem:'))
elif programa_escolhido =='area':
    area()
elif programa_escolhido =='contador':
    contador()
elif programa_escolhido == 'maior':
    maior(5,2,3,54)
else:
    print('Não é uma programa válido.')
