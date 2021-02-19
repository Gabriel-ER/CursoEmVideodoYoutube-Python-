#Fatiamento
frase="Curso em video Python"
'''
print(frase[9]) #mostra a décima string (começa do 0)
print(frase[9:14]) #mostra entre a décima e a décima terceira string
print(frase[-2]) #mostra a penúltima string
print(frase[0:22:2]) #Começa na posição 0, vai até a 22 e o passo, step, é de dois em dois.
print(frase[1:22:2])
print(frase[:22:1]) #posso omitir o início para ser 0. O step não pode ser 0.
print(frase[9::3]) #Começa no 9 e vai até o final de 3 em 3
'''
'''
print(len(frase))
print("borogodo".count('o'))#conta as ocorrências do "o" minúsculo.
print(frase.count('o',0,13))#contagem com fatiamento
print(frase.find('deo')) #mostra onde uma cadeia específica de caracteres começa
print(frase.find('android')) #Retorna -1 se não for encontrado
print('Curso' in frase) #Retorna verdadeiro se a sequência estiver presente
lista=[1,2,3,4,5,6]
print(7 in lista)
'''

'''
#Transformação de strings
frase="Curso em Video python"
nova_frase=frase.replace('Python','Android')#Não altera a string tratada. Apenas reordena momentaneamente.
print(nova_frase)

frase_maiuscula=frase.upper()
print(frase_maiuscula) #Não altera a string

frase_minuscula=frase.lower() #Nao altera a string
print(frase_minuscula)

frase_captalizada=frase.capitalize() #Todos os caracteres são transformados em minúsculos e depois o primeiro em maiúscula
print(frase_captalizada)

frase_em_title=frase.title() #Todos os inícios de palavra são colocados em maiúscula
print(frase_em_title)

frase2="   Tomar cerveja        "
frase_estripada=frase2.strip() #remove todos os espaços no início e no final da string
#remover somente os espaços do lado direito: frase2.rstrip
#remover somente os espaços do lado esquerdo: frase2.lstrip
print(frase_estripada)
print(frase2)
print(frase2[4],frase_estripada[4])
'''


print(frase.split()) #separa cada palavra em uma nova string
print('--'.join(frase))
print('--'.join(frase.split()))
