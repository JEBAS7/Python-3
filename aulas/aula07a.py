nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome}!')
print(f'Prazer em te conhecer {nome:20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d}')
print(f'Divisão inteira {di} e potência {e}')
