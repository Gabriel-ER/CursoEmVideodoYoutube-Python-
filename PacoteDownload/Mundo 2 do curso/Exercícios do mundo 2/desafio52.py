num=int(input(':'))
ultimo = 0
for candidato in range (1,num+1,2):
    numDivisores=0
    for i in range(1,int((candidato+1)/(1/2))):
        if candidato % i == 0:
            numDivisores = numDivisores+1
    if numDivisores == 2:
        ultimo = candidato
print(ultimo)
