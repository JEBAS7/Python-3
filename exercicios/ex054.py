from datetime import date

hoje = date.today().year
menoridade = 0
maioridade = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = hoje - ano
    if idade < 18:
        menoridade += 1
    else:
        maioridade += 1
print(f'Tem {menoridade} pessoas menores de idade.')
print(f'Tem {maioridade} pessoas maiores de idade')


