def somar(x,y):
    soma = x+y
    print("A soma é{}".format(soma))
    return 0

def multiplicar(x,y):
    multiplicacao = x*y
    print("A multiplicacao é{}".format(multiplicacao))
    return 0

def novos_numeros():
    j=float(input("Digite o número novo:"))
    return j
def maior(x,y):
    if x > y:
        print("O maior é {}".format(x))
    else:
        print("O maior é {}".format(y))
    return 0

def sair():
    exit()
    return 0

val_1=float(input("Digite o valor 1:"))
val_2=float(input("Digite o valor 2:"))
print("""
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa

""")
opcao=int(input("Opcao ou sair:"))
if opcao == 1:
    somar(val_1,val_2)
elif opcao == 2:
    multiplicar(val_1, val_2)
elif opcao == 3:
    maior(val_1,val_2)
elif opcao == 4:
    j=novos_numeros()
    print(j)
elif opcao == 5:
    sair()