from datetime import date

ano = int(input('Qual é o ano que você nasceu? '))
atual = date.today().year
idade = date.today().year - ano
if idade < 18:
    data = 18 - idade
    print(f'Você tem {idade} anos de idade, pode se alistar em {data} anos')
    alist = atual + data
    print(f'Seu alistamento será em {alist}')
elif idade == 18:
    print(f'Você já tem {idade} anos de idade e deve se alistar IMEDIATAMENTE!.')
else:
    data = idade - 18
    print(f'Você tem {idade} anos de idade, já passou {data} anos para se alistar.')
    alist = atual - data
    print(f'Seu alistamento foi em {alist}')
