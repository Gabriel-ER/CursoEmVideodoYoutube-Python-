frase = input("Digite sua frase:\n").lower().strip()
ocorrencias = frase.count("a")
print(ocorrencias)
print("A primeira ocorrência de a é {}".format(frase.find("a")))

print("A última ocorrência de a é {}".format(frase.find("a",-1)))
print("A última ocorrência de a é {}".format(frase.rfind("a")))

