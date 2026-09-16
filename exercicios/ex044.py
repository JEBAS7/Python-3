preco = float(input('Digite o preço do produto: '))
print('Forma de pagamento\n'
      'Digite 1 para dinheiro ou cheque a vista\n'
      'Digite 2 para cartão a vista\n'
      'Digite 3 para 2x no cartão\n'
      'Digite 4 para 3x ou mais no cartão')
pagamento = int(input('Como você vai pagar? '))
if 1:
    valor = preco - preco * 10 / 100
    print(f'Com 10% de desconto a vista o preço é {valor} ')
if 2:
    valor = preco - preco * 5 / 100
    print(f'Com 5 de desconto a vista no cartão o preço é {valor}')
if 3:
    print(f'Com 2x no cartão o preço é {preco}')
if 4:
    valor = preco + preco * 20 / 100
    print(f'Com 3x ou mais no cartão tem 20% de juros e o preço é {valor}')