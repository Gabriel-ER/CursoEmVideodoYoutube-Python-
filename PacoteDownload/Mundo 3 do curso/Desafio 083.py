expressao = ''.join(input("Digite sua expressão:").strip().split())
print(expressao)
lista=[]
parenteses_abertos = expressao.count('(')
parenteses_fechados = expressao.count(')')

if parenteses_abertos > parenteses_fechados:
    print("Faltou fechar")
elif parenteses_fechados > parenteses_abertos:
    print("Faltou abrir")
else:
    print("Certinho")
print(f'{parenteses_abertos}')
print(f'{parenteses_fechados}')
