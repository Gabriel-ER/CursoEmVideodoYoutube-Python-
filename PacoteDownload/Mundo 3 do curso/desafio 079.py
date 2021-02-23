a=[]
r=''

while True:
    j=int(input("Digite um número"))

    if j in a:
        print(f"{j} já está na lista")
    else:
        a.append(j)



    r=input("Digite ENTER para continuar.")


    if r != '':
        break
print(F'Sua lista: {a}')