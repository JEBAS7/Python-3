loja = 'LOJA BISPO'
print(f'{loja:=^50}')
p = float(input('Digite o preço R$'))
d = p - p * 5 / 100
print(f'O preço do produto com desconto de 5% é {d}')