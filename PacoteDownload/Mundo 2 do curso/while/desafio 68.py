contador_de_vitorias=0
while True:
    from random import randint
    print('=-'*10)
    print("Vamos jogar Par ou Impar")
    print('=-'*10)
    escolha_pc=randint(1,1000)
   # print(escolha_pc)
    escolha_jogador=int(input("Digite seu valor: "))
    soma=escolha_jogador+escolha_pc
    par_ou_impar=input("Par ou Impar? ").upper().strip()
    if par_ou_impar in 'PARP':
        if soma % 2 ==0:
            print(f"{soma} é Par e Você venceu!!!!!")
            contador_de_vitorias += 1
            print(f'{contador_de_vitorias} Vitórias')
        else:
            print(f'Você perdeu com {contador_de_vitorias} vitorias')
    else:
        if soma % 2 !=0:
            print(f"{soma} é Impar e Você venceu!!!!!")
            contador_de_vitorias += 1
            print(contador_de_vitorias)
        else:
            print(f'Você perdeu com {contador_de_vitorias} vitorias')
            break

