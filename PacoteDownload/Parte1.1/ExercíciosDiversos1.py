numero_exercicio=int(input("exercício:"))
if numero_exercicio==1:
    #Mostra a parte inteira
    import math
    numero=float(input("Digite o número:\n"))
    truncado=math.trunc(numero)
    print(truncado)

elif numero_exercicio==2:
    #calculado hipotenusa
    from math import sqrt
    c1=float(input("Cateto1:\n"))
    c2=float(input("Cateto2:\n"))
    hipotenusa=sqrt((c1**2)+(c2**2))
    print("{:.3f}".format(hipotenusa))

elif numero_exercicio==3:
    #Dê-me o ângulo e eu lhe dou o sin o cos e a tan
    import math

    angulo=math.radians(float(input("Angulo:\n")))
    seno=math.sin(angulo)
    cosseno=math.cos(angulo)
    tangente=math.tan(angulo)
    print("seno: {:.2f} cos: {:.2f} tan: {:.2f}".format(seno,cosseno,tangente),end=' final de programa')

elif numero_exercicio==4:
    #Escolha aleatória de alunos
    import random
    a1=input("aluno1:\n")
    a2=input("aluno2:\n")
    a3=input("aluno3:\n")
    a4=input("aluno4:\n")
    
    escolhido=random.randint(1,4) #Escolhe um número entre 1 e 4
    funcao=int(input("digite a função que deseja:\n"))
    if funcao==1: #Se digitar 1, função escolher aluno. Outro número vai pra outra função
        if escolhido==1:
            print("O escolhido foi {}".format(a1))
        else:
            if escolhido==2:
                print ("O escolhido foi {}".format(a2))
            else:
                if escolhido==3:
                    print("O escolhido foi {}".format(a3))
                else:
                    print("O escolhido foi {}".format(a4))
    else:
        lista=[a1,a2,a3,a4]
        random.shuffle(lista)
        print(lista)
elif numero_exercicio == 5:
    #outro modo de fazer o exercício 4
    from random import shuffle
    a1=input("a1:\n")
    a2=input("a2:\n")
    a3=input("a3:\n")
    a4=input("a4:\n")
    lista=[a1,a2,a3,a4]
    #reordenando lista
    shuffle(lista)
    print(lista)