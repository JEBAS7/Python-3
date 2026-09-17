numero = int(input('Digite um número: '))
print('-1 para binário\n-2 para octal\n-3 para hexadecimal')
base = int(input('Qual é a base de conversão? '))
if base == 1:
    binario = bin(numero)[2:]
    print(f'O número {numero} para binário é {binario}')
elif base == 2:
    octal = oct(numero)[2:]
    print(f'O número {numero} para octal é {octal}')
elif base == 3:
    hexadecimal = hex(numero)[2:]
    print(f'O número {numero} para hexadecimal é {hexadecimal}')
else:
    print('Base inválida! tente novamente.')
