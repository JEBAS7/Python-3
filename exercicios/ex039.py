from datetime import date
ano = int(input('Qual é o ano que você nasceu? '))
idade = date.today().year - ano
if idade < 18:
    data = 18 - idade
    print(f'Você tem {idade} anos de idade, pode se alistar em {data} anos')
elif idade == 18:
    print(f'Você já tem {idade} anos de idade e pode se alistar.')
else:
    data = idade - 18
    print(f'Você tem {idade} anos de idade, já passou {data} anos para se alistar.')
