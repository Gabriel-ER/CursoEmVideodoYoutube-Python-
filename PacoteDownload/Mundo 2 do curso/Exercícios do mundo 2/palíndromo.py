entrada = (str(input(":_")).lower().strip()).split()
palavra = ''.join(entrada)
saida=''
#for i in range(-1, -len(palavra)-1, -1):
for letra in range(len(palavra)-1, -1, -1):
    print(palavra[letra])
    saida += palavra[letra]
    #saida = saida + palavra[letra]
if saida == palavra:
    print('ok')
else:
    print('not ok')


# print(list(range(len(palavra)+1)))
print(palavra)
print(saida)
