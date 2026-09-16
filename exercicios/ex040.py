n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'A média do aluno é {media}, ele está aprovado!')
elif media >= 5 and media < 6.9:
    print(f'A media do aluno é {media}, ele está em recuperação!')
else:
    print(f'A média do aluno é {media}, ele está reprovado!')