num = int(input('Digite um número: '))
tot = 0  # Contador de divisores

for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')  # Amarelo se for divisor
        tot += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')  # Vermelho se não for divisor

print(f'\nO número {num} foi dividido {tot} vezes.')

if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
