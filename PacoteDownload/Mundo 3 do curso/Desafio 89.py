lista=[]
contador = 1
resposta = ''
while True:
    nome_aluno = input(f'Nome do alun {contador}: ')
    nota1_aluno = int(input('Nota 1: '))
    nota2_aluno = int(input('Nota 2: '))

    lista.append([])
    lista[contador-1].append(nome_aluno)
    lista[contador-1].append(nota1_aluno)
    lista[contador-1].append(nota2_aluno)
    contador += 1
    print(lista)
    resposta = input('Continuar?')
    if resposta in 'NnNão':
        contador = 0
        break

for aluno in lista:
    media = (aluno[1]+aluno[2])/2
    aluno.append(media)
    print(f'{contador}:  Nome: {aluno[0]} | Nota 1: {aluno[1]} | Nota 2: {aluno[2]} Média: {media}')
    contador += 1
resposta = int(input('Qual deseja consultar? '))

print(f'Nome: {lista[resposta][0]} | Nota 1: {lista[resposta][1]} | Nota 2: {lista[resposta][2]} Média: {lista[resposta][3]}')