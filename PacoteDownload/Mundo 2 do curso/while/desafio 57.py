sexo = input("Digite o sexo [M/F]:").upper().strip()[0]
aceitaveis = ['M', 'F']

#Outra forma de fazer:
#while sexo not in "MmFf"

while not(sexo in aceitaveis):
    print("Digite uma opção válida! [M/F]")
    sexo = input("Digite o sexo [M/F]:").upper().strip()[0]
print("FIM")
