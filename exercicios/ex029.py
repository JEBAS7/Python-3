v = float(input('Qual a velocidade do carro: '))
m = (v - 80) * 7.0
if v > 80:
    print(f'Voce ultrapassou o limite de velocidade! foi multado em R${m:.2f}!')
else:
    print('Você está dirigindo bem! Boa viagem!')
