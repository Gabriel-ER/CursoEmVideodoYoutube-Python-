'''
valorCasa=int(input('Valor da casa:'))
salario =float(input('Seu salário:'))
anos = int(input('Anos:'))

prestacaoMensal= valorCasa/(anos*12)
if prestacaoMensal <= salario*0.3:
    print('aprovado!')
else:
    print('Reprovado')
'''

numero = int(input('numero: '))

opcao = int(input('opcao: '))

print('1 para bin, 2 para oct e 3 para hex')
if opcao == 1:
    print('{} em binário é {}: '.format(numero, str(bin(numero)).removeprefix('0b')))
elif opcao == 2:
    print('{} em binário é {}: '.format(numero, str(oct(numero)).removeprefix('0o')))
elif opcao == 3:
    print('{} em binário é {}'.format(numero, str(hex(numero)).removeprefix('0x')))

