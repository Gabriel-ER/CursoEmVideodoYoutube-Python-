nome = input("Digite o seu nome:\n").lower().strip()
listaNomes = ['ana', 'maria', 'joão', 'pedro']
if nome == 'gabriel':
    print('Você vai ser muito gostoso.')
elif nome in listaNomes:
    print('{} é um nome muito popular no Brasil'.format(nome.capitalize()))
print("Tenha um bom dia, {}!".format(nome.capitalize()))