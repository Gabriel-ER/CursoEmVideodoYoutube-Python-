def voto(ano_de_nascimento, analfabeto='N'):
    from datetime import datetime, date

    analfabeto = analfabeto.upper()
    # posso pegar o ano também com:
    idade = date.today().year - ano_de_nascimento
    # idade = datetime.now().year - ano_de_nascimento
    print(f'Idade: {idade} anos.')
    if idade < 16:
        return 'Voto proibido'
    if 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos, o Voto é Opicinal'
    if 18 <= idade < 70:
        if analfabeto == 'S':
            return 'Voto opicional por ser analfabeto.'
        else:
            return f'Com {idade} anos, o Voto é obrigatório '


ano_de_nascimento = int(input('Ano de nascimento: '))
print(voto(ano_de_nascimento, 'n'))
