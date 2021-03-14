def fatorial(número, show=True):
    """

    :param número: Fatoriando
    :param show: Mostra os detalhes da conta
    :return: Retorna o Fatorial
    """

    temporario = número
    c = 1
    fatorial = 1
    if show == True:
        print(número, end=' x ')
    while c < número:

        if número-c != 720:
            if show == True:
                if número-c != 1:
                    print(número - c, end=' x ')

                else:
                    print(número - c, end=' = ')
        temporario *= (número - c)
        c += 1

    return temporario
print(fatorial(10,True))