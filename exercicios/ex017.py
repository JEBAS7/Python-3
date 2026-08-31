from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
x = hypot(co, ca)
print(f'O comprimento da hipotenusa é {x:.2f}')
