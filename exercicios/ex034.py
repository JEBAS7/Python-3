s = float(input('Digite o salário: '))
if s > 1250:
    a1 = s + s * 10 / 100
    print(f'Com 10% de aumento do salário R${s:,.2f} vai ser R${a1:,.2f}')
if s < 1250:
    a2 = s + s * 15 / 100
    print(f'Com 15% de aumento do salário R${s:,.2f} vai ser R${a2:,.2f}')
