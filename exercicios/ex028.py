from random import randint
from time import sleep
cpu = randint(0, 5)
print('-=' * 20)
print('Vou pensar em um número entre 0 e 5.')
print('-=' * 20)
n = int(input('Escolha um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if cpu == n:
    print(f'Parabéns! você venceu o número escolhido foi {cpu} ')
else:
    print(f'Você perdeu! O número escolhido foi {cpu}')
