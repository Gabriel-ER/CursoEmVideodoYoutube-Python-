import math
#ESTRUTURA DE USO: modulo.função()

#from math import sqrt

numero=int(input("Digite o número:"))
#raiz=sqrt(numero)
raiz=math.sqrt(numero)



#Se eu não fizer o import geral do módulo (import math) e só fizer o import
#da função (from math import sqrt), não preciso usar math.sqrt
#Posso usar somente sqrt

print("A raiz de {} é igual a {:.2f}".format(numero,raiz))