num = int(input("Digite um número até 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f"unidade: {u}")
print(f"dezena: {d}")
print(f"centena: {c}")
print(f"milhar: {m}")
