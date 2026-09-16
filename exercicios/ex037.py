numero = int(input('Digite um número: '))
print('-1 para binário\n-2 para octal\n-3 para hexadecimal')
base = int(input('Qual é a base de conversão? '))
if base == 1:
    binario = bin(numero)
    print(f'O número {numero} para binário é {binario}')
if base == 2:
    octal = oct(numero)
    print(f'O número {numero} para octal é {octal}')
if base == 3:
    hexadecimal = hex(numero)
    print(f'O número {numero} para hexadecimal é {hexadecimal}')
