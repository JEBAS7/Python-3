valor_casa = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é o seu salário: '))
anos = int(input('Em quantos anos você vai pagar: '))
mensalidade = valor_casa / (anos * 12)
limite = salario * 0.30
if mensalidade <= limite:
    print(f'Empréstimo aprovado com {mensalidade:.2f} por mes em {anos} anos!')
else:
    print('Empréstimo negado!')
