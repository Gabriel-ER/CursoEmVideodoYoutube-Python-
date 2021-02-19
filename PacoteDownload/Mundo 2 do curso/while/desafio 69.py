# programa de cadastro de pessoas
def cadastro():
    idade = [0]
    sexo = ['']
    y = [0] #será somada ao fim de idade para possibilitar que cumente a lista
    u = ['']
    i = 0
    maiores = 0
    homens = 0
    mulheres = 0

    while True:
        continuar=input("Digite enter para continuar: ")
        if continuar != '':
            print(f'{maiores} maiores, {homens} homens, {mulheres} mulheres')
            break

        else:
            idade[i] += int(input('Digite a idade: '))  # Sobrescreve o valor à direita na casa indicada à esquerda
            if idade[i] > 18:
                maiores += 1
            sexo[i] += input('Digite o sexo: [M/H] ').upper().strip()
            if sexo[i] in 'MmFf':
                mulheres += 1
            else:
                homens += 1
            print(f'Idade: {idade}')
            print(f'Sexo: {sexo}')

            i += 1  # Muda o índice que será sobrescrito.
            idade += y
            sexo += u
            """A lista só pode ser reindexada até o tamanho definido lá em cima
             Neste caso, 1 elemento. Ao adicionar a lista y ao final de cada
             iteração, posso prosseguir adicionando indefinidamente."""
#=====================================================================
cadastro()

