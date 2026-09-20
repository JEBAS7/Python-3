maior_peso = 0
menor_peso = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'A pessoa de maior peso é {maior_peso}Kg')
print(f'A pessoa de menor peso é {menor_peso}Kg')
