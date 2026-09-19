n = int(input('Digite um número para ver sua tabuada: '))
t = 'TABUADA'
print(f'{t:=^15}')
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
print(f'=' * 15)
