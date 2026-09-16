a = float(input('Digite a reta a: '))
b = float(input('Digite a reta b: '))
c = float(input('Digite a reta c: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print(f'As retas a = {a} e b = {b} e c = {c} formam um triângulo equilátero.')
    elif a == b != c or a == c != b or b == c != a:
        print(f'As retas a = {a} e b = {b} e c = {c} formam um triângulo isósceles.')
    else:
        print(f'As retas a = {a} e b = {b} e c = {c} formam um triângulo escaleno.')
else:
    print(f'As retas a = {a} e b = {b} e c = {c} não formam um triângulo.')