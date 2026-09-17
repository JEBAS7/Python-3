from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Tem {idade} anos de idade, classificação MIRIM.')
elif idade <= 14:
    print(f'Tem {idade} anos de idade, Classificação INFANTIL.')
elif idade <= 19:
    print(f'Tem {idade} anos de idade, classificação JUNIOR.')
elif idade <= 25:
    print(f'Tem {idade} anos de idade, classificação SÊNIOR.')
else:
    print(f'Tem {idade} anos de idade, classificação MASTER.')
