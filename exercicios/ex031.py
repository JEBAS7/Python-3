d = int(input('Qual a distância da viagem: '))
if d <= 200:
    print(f'O valor da passagem é R${d * 0.50:.2f}')
else:
    print(f'O valor da passagem é R${d * 0.45:.2f}')
