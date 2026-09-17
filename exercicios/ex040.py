n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'Tirando {n1} e {n2} a média do aluno é {media}, ele está APROVADO!')
elif 7 > media >= 5:
    print(f'Tirando {n1} e {n2} a media do aluno é {media}, ele está em RECUPERAÇÃO!')
else:
    print(f'Tirando {n1} e {n2} a média do aluno é {media}, ele está REPROVADO!')