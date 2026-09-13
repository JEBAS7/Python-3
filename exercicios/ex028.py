from random import randint

cpu = randint(0, 5)
n = int(input('Escolha um número de 0 a 5: '))
if cpu == n:
    print(f'Parabéns! você venceu o número escolhido foi {cpu} ')
else:
    print(f'Você perdeu! O número escolhido foi {cpu}')
