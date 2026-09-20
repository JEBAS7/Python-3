soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
garota = 0

for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    soma_idade += idade

    # Lógica para encontrar o homem mais velho
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    # Lógica para contar mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        garota += 1

media = soma_idade / 4

print(f'\nA média de idade do grupo é {media:.1f} anos.')
if nome_velho != '':
    print(f'O homem mais velho é o {nome_velho} com {maior_idade_homem} anos.')
else:
    print('Não foram digitados homens no grupo.')
print(f'Tem {garota} mulheres com menos de 20 anos.')
