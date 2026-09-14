v = float(input('Qual a velocidade do carro: '))
m = (v - 80) * 7
if v > 80:
    print(f'\033[0;31mVoce ultrapassou o limite de velocidade de 80km/h! Foi multado em R${m:.2f}!\033[0m')
print('Você está dirigindo bem! Boa viagem!')
