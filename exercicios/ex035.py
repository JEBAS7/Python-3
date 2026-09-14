a = float(input('Digite a reta a: '))
b = float(input('Digite a reta b: '))
c = float(input('Digite a reta c: '))
if a < b + c and b < a + c and c < a + b:
    print(f'As retas a = {a} e b = {b} e c = {c} formam um triângulo.')
else:
    print(f'As retas a = {a} e b = {b} e c = {c} não formam um triângulo.')
