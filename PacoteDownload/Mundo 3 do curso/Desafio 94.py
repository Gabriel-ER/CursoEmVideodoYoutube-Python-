pessoas = []
contador = 0

while True:
    pessoas.append({})
    pessoas[contador]['Nome'] = input(f'Nome {contador}: ')

    pessoas[contador]['Sexo'] = input('Sexo: ').upper()[0]
    while pessoas[contador]['Sexo'] not in 'FM':
        print('Digite um sexo válido!')
        pessoas[contador]['Sexo'] = input('Sexo: ').upper()[0]

    pessoas[contador]['Idade'] = int(input('Idade: '))
    print(f'cadastrado: {pessoas[contador]}')
    contador += 1

    resposta = input('Continuar? [S/N] ').upper()
    while resposta not in 'SN':
        print('Resposta inválida. [S/N]')
        resposta = input('Continuar? [S/N]')
    if resposta[0] == 'N':
        print(f'Pessoas: {pessoas}')
        break
# Uma lista para teste para não precisar digitar tudo
'''pessoas = [{'Nome': 'Gabriel', 'Sexo': 'M', 'Idade': 24},
           {'Nome': 'João', 'Sexo': 'M', 'Idade': 40},
           {'Nome': 'Helena', 'Sexo': 'F', 'Idade': 38},
           {'Nome': 'Maria', 'Sexo': 'F', 'Idade': 7},
           {'Nome': 'Maria Clara', 'Sexo': 'F', 'Idade': 25}]'''

tot_idade = 0
for p in pessoas:
    tot_idade += p['Idade']

mulheres = []
for m in pessoas:
    if m['Sexo'] == ('F' or 'f'):
        mulheres.append(m)
acima_da_media = []
for a in pessoas:
    if a['Idade'] > tot_idade / len(pessoas):
        acima_da_media.append(a)

print(f'A: {len(pessoas)} pessoas cadastradas')
print(f'B: A média das idades é {tot_idade / (len(pessoas)):5.2f} anos.')

print('C: Mulheres: ', end=' ')
for mulher in mulheres:
    print(f'{mulher["Nome"]},', end=' ')
print()

print('D: Pessoas com idade acima da média: ', end=' ')
for velho in acima_da_media:
    print(f'{velho["Nome"]},', end=' ')
print()
