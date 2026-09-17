print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Digite o preço do produto: R$'))
print('''FORMAS DE PAGAMENTO
Digite 1 para dinheiro ou cheque a vista
Digite 2 para cartão a vista
Digite 3 para 2x no cartão
Digite 4 para 3x ou mais no cartão''')
pagamento = int(input('Como você vai pagar? '))
if pagamento == 1:
    valor = preco - preco * 10 / 100
    print(f'Com 10% de desconto a vista o preço é R${valor:.2f} ')
elif pagamento == 2:
    valor = preco - preco * 5 / 100
    print(f'Com 5% de desconto a vista no cartão o preço é R${valor:.2f}')
elif pagamento == 3:
    parcela = preco / 2
    print(f'Com 2x no cartão o preço é R${preco:.2f} e cada parcela é R${parcela:.2f}')
elif pagamento == 4:
    total_parcelas = int(input('Em quantas parcelas'))
    valor = preco + preco * 20 / 100
    parcela = valor / total_parcelas
    print(f'Com {total_parcelas}x no cartão, tem 20% de juros. O preço é R${valor:.2f} em {total_parcelas}x de R${parcela:.2f}')
else:
    print(f'Erro! você digitou {pagamento}, não exite essa forma de pagamento.')
