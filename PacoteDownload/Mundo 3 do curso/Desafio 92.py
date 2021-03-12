
from datetime import datetime
trabalhador = {'Nome:':input('Nome: '), 'Nascimento YYYY ' : int(input('Ano de nascimento YYYY: ')), 'CTPS':int(input('Carteira de trabalho: '))}
trabalhador['Idade'] = datetime.now().year - trabalhador['Nascimento YYYY ']

# trabalhadores = {'Nome:': 'Gabriel', 'Nascimento YYYY': 1997, 'CTPS': 2525, 'Contratação': 2000, 'Salário': 5000.0}

if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Digite o ano de contratação YYYY: '))
    trabalhador ['Salário'] = float(input('Digite o salário: R$ '))
    trabalhador['Idade_aposentadoria'] = (trabalhador['Contratação'] + 35) - trabalhador['Nascimento YYYY ']



print(trabalhador)
for k,v in trabalhador.items():
    print(f'{k}: {v}')
