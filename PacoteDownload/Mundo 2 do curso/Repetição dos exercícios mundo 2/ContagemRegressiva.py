# contador regressivo de 1 em 1 segundo
'''from time import sleep,time
for i in range (10, -1, -1):
    print(i)
    sleep(1)
    print(time())
print("Kabum")'''

# Enumarador dos pares entre 1 e 50
'''
for i in range (2,51,2):
    print(i)
'''

# soma dos ímpares múltiplos de 3 entre 1 e 500
"""
s=0
for i in range(1,500):
    if i%3==0:
        s+=i
print(s) 
"""

# somador de entradas pares
'''
soma=0
for i in range(6):
    n = int(input("número \n:"))
    if n%2==0:
      soma+=n
print(soma)
'''

# identificador de primos
'''
n=int(input("digite seu número\n:"))
if n%2==0:
    print("não é primo")
divisores=0
for i in range (0+1,int(n/2)):
    if n%i==0:
        divisores+=1
if divisores < 2:
    print("primo")
'''

# identificador de palíndromoss
'''frase=input("frase:\n").upper().strip().split()
junto=''.join(frase)
print(junto)
contrario=""
for i in range(len(junto)-1,-1,-1):
    #print(junto[i])
    contrario += junto[i]
print(contrario)
if contrario==junto:
    print("palindromo")'''

# identificador de palindromos 2

'''frase=input("frase:\n").upper().strip().split()
junto=''.join(frase)
inverso = junto[::-1]
print(inverso)'''
a="{} {} {}".format(input("1"),input("2"),input("3"))
print(a)