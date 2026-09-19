from time import sleep

print('=' * 25)
print(' 10 TERMOS DE UMA P.A. ')
print('=' * 25)

# 1. Lendo os dados informados pelo usuário
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))

# 2. Calculando matematicamente qual será o 10º termo
# Usamos a fórmula: an = a1 + (n - 1) * r
decimo = primeiro + (10 - 1) * razao

# 3. Laço que percorre do primeiro até o décimo termo
# Adicionamos '+ razao' no limite superior porque o range() é exclusivo
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')
    sleep(1)
print('ACABOU!')
