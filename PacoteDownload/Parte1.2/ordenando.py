n1=int(input("n1:"))
n2=int(input("n2:"))
n3=int(input("n3:"))
lista=[n1,n2,n3]
print("lista original:", lista)
if n1<n2 and n2<n3:
    print("ordenado:{}".format(lista))
else:
    if n1>n2:
        lista[0]=n2
        lista[1]=n1
        if n1>n3:
            lista[1]=n3
            lista[2]=n1
    else:
        if n3 < n1:
            lista[0] = n3
            lista[2] = n1
print(lista)

