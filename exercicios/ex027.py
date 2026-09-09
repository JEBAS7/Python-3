nome_completo = input("Digite seu nome completo: ").strip()

# Transforma o nome em uma lista de palavras
n = nome_completo.split()

# Mostra os resultados
print(f"Muito prazer em te conhecer! {n[0]}")
print(f"Seu primeiro nome é {n[0]}")
print(f"Seu último nome é {n[-1]}")
