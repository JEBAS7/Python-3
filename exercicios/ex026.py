# Lê a frase, remove espaços inúteis e joga tudo para maiúsculo
frase = input("Digite uma frase: ").strip().upper()

# 1. Quantas vezes aparece a letra "A"
print(f"A letra A aparece {frase.count('A')} vezes na frase.")

# 2. Em que posição ela aparece a primeira vez (somamos 1 para ficar humano)
print(f"A primeira letra A apareceu na posição {frase.find('A') + 1}")

# 3. Em que posição ela aparece a última vez (rfind busca da direita para a esquerda)
print(f"A última letra A apareceu na posição {frase.rfind('A') + 1}")
