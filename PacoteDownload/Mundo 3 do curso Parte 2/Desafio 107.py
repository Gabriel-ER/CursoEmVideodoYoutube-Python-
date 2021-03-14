"""import Moeda
p = float(input('Digite o preço: R$').replace(',','.'))
print(f'A metade de {Moeda.formato_moeda(p)} é {Moeda.formato_moeda(Moeda.metade(p))}')
print(f'O dobro de {Moeda.formato_moeda(p)} é {Moeda.formato_moeda(Moeda.dobro(p)) }')
print(f'Um aumento de 10% sobre {Moeda.formato_moeda(p)} é {Moeda.formato_moeda(Moeda.aumentar(p))}')
print(f'Um desconto de 10% sobre {Moeda.formato_moeda(p)} é {Moeda.formato_moeda(Moeda.diminuir(p))}')
"""
import Moeda

p = float(input('Digite o preço: R$').replace(',', '.'))
'''aumento = 25
diminuição = 25
print(f'A metade é {Moeda.metade(p, True)}')
print(f'O dobro é {Moeda.dobro(p, True)}')
print(f'Um aumento de {aumento}% é {Moeda.aumentar(p,aumento, True)}')
print(f'Um desconto de {diminuição}% é {Moeda.diminuir(p, diminuição, True)}')'''
Moeda.resumo(p,25,50)
