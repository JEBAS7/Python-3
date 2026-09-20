# Lê a frase e remove os espaços das extremidades
frase = str(input('Digite uma frase: ')).strip().upper()

# Divide a frase em uma lista de palavras e junta tudo sem espaços
palavras = frase.split()
frase_junta = ''.join(palavras)

frase_invertida = ''

# Loop para inverter a frase de trás para frente
for letra in range(len(frase_junta) - 1, -1, -1):
    frase_invertida += frase_junta[letra]

print(f'O inverso de {frase_junta} é {frase_invertida}.')

# Verifica se formam a mesma frase
if frase_invertida == frase_junta:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
