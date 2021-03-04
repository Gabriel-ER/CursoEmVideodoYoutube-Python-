aluno = {}
aluno['Nome'] = input('Nome:')
aluno['Média'] = float(input(f"Média de {aluno['Nome']} "))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print(aluno)
print('-=' *30)
for k, v in aluno.items():
    print(f' {k} é {v}')
    print()