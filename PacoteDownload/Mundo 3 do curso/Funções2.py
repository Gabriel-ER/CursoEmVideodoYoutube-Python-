# --------------------
# Entendendo docstrings
# --------------------
def contador(i, f, p):
    """

    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    """
    from time import sleep
    c = i
    while c < f + 1:
        print(f'{c}', end=' ')
        sleep(0.5)
        c += p
    print('FIM!')


# help(contador)


# ---------------------------------
# Entendendo parâmetros opicionais:
# ---------------------------------

def somar(a, b, c=0):  # 'c = 0' torna o parâmetro 'c' opicional. Posso tornar todos os parâmetros opicionais
    s = a + b + c
    print(f'A soma vale {s}')


def multipicar(a, b, c=1):
    m = a * b * c
    print(f'A multipicação vale {m}')


def multiplicar2(*num):  # O comando recebe um número indefinido de variáveis.
    print(num)


# multiplicar2(2,3,4,5,6,7)


# ---------------------------------
# Entendendo escopo global e local
# ---------------------------------

'''Escopo global
    Na função abaixo, a variável n
    valerá para todos os programas onde aparecer'''


def teste():
    x = 8  # variável local
    print(f'Na função teste, n vale {n}')


n = 10  # variável global
# print(x) # x é uma variável local da definição da função teste. Logo, não
# existe aqui fora.
teste()

'''O comando 'global' faz com que um variável definida dentro
de um escopo local tenha validade global'''


def teste2(b):
    global a  # comente para 'a' se tornar uma variável local
    # a = 8 # o que eu fizer com 'a' aqui será feito lá fora
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


'''a = 5
teste2(a)
print(f'A fora vale {a}')'''


# ---------------------------------
# Entendendo o retorno de uma função
# ---------------------------------

def somar2(a, b, c=0):  # 'c = 0' torna o parâmetro 'c' opicional. Posso tornar todos os parâmetros opicionais
    s = a + b + c
    #print(f'A soma vale {s}')
    return s # Agora posso utilizar o resultado da minha função

print(somar2(2,3) + somar2(5,7))
