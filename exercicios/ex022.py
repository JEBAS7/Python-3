nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
n = nome.split()
print(f'Seu nome completo tem {len(''.join(n))} letras')
pn = nome.split()[0]
print(f'Seu primeiro nome tem {len(pn)} letras')
