compras=["batata","alface","cebola"]
compras[1]=False
print(compras)


lista2=("a","b","c","d")
#tuples não aceitam modificações
print(lista2[2])

#dicionários. Muito importante lembrar que dicionários são declarados com {} chaves.
relacionamentos={"Nathália":"amor da minha vida","doralice":"mãe linda que eu amo","Gabi":"Irmã zé droguinha"}
print(relacionamentos)
print("Nathália é",relacionamentos["Nathália"])

for chave in relacionamentos:
    #print(chave)
    print(relacionamentos[chave])

for i in relacionamentos.keys():
    print(i)
    print(relacionamentos.items())