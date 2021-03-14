def notas(*notas,sit=False):
    """

    :param notas: Digite quantas notas o aluno possuir
    :param sit: Decalrar ou não a situação do aluno?
    :return: retorna as notas e a situação (se sit = True)
    """
    dicionário = {}
    notas = list(notas)
    total = 0
    for i in notas:
        total += i
    dicionário['Total'] = total
    dicionário["Maior"] = max(notas)
    dicionário["Menor"] = min(notas)
    dicionário['Média'] = total/len(dicionário)
    if sit == True:
        if dicionário['Média'] >=7:
            dicionário['Situação'] = 'Aprovado'
            return dicionário
        else:
            dicionário['Situação'] = 'Reprovado'
            return dicionário



notas(3,0,4,10, sit=True)
print(notas(3,0,4,10, sit=True))