peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Você está com {imc:.2f} de IMC, você está abaixo do peso.')
elif imc < 25:
    print(f'Você está com {imc:.2f} de IMC, você está com peso ideal.')
elif imc < 30:
    print(f'Você está com {imc:.2f} de IMC, você está com sobrepeso.')
elif imc < 40:
    print(f'Você está com {imc:.2f} de IMC, você está com obesidade.')
else:
    print(f'Você está com {imc:.2f} de IMC, você está com obesidade mórbida.')
    