def aumentar(x,y=10, formatação = False):
    if formatação == True:
        return formato_moeda((1+(y/100))*x)
    else:

        return (1+(y/100))*x

def diminuir(x, y=10, formatação = False):
    if formatação == True:
        return formato_moeda((1-(y/100))*x)
    else:
        return (1-(y/100))*x

def dobro(x, formatação = False):
    if formatação == True:
        return formato_moeda(2 * x)
    else:
        return 2 * x

def metade(x, formatação = False):
    if formatação == True:
        return formato_moeda(0.5 * x)
    else:
        return 0.5 * x

def formato_moeda(preço,moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo(preço, aumento, redução):
    print(
    f"""
    -------------------------------------------------
            Resumo do Valor
    -------------------------------------------------
    Preço Analisado:            {formato_moeda(preço)}
    Dobro:                      {dobro(preço,True)}
    Metade                      {metade(preço, True)}
    {aumento}% de aumento:             {aumentar(preço,aumento,True)}
    {redução}% de redução:             {diminuir(preço,redução, True)}
    -------------------------------------------------
    
    """)