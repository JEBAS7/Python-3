from random import choice
from time import sleep

print('\033[1;33m-=\033[m' * 30)
print('{:^70}'.format('\033[1;31m JOKENPÔ \033[m'))
print('\033[1;33m-=\033[m' * 30)
jogador = str(input('Escolha PEDRA, PAPEL, TESOURA: ')).strip().upper()
cpu = choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('\033[1;33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!\033[m')
sleep(1)
if cpu == jogador:
    print(f'Computador escolheu {cpu}, Jogador escolheu {jogador}')
    print('Jogo empatou!')
elif cpu == 'PEDRA' and jogador == 'PAPEL':
    print(f'Computador escolheu {cpu}. Jogador escolheu {jogador}')
    print('\033[1;32mJogador venceu!\033[m')
elif cpu == 'PAPEL' and jogador == 'TESOURA':
    print(f'Computador escolheu {cpu}. Jogador escolheu {jogador}')
    print('\033[1;32mJogador venceu!\033[m')
elif cpu == 'TESOURA' and jogador == 'PEDRA':
    print(f'Computador escolheu {cpu}. Jogador escolheu {jogador}')
    print('\033[1;32mJogador venceu!\033[m')
else:
    print(f'Computador escolheu {cpu}. Jogador escolheu {jogador}')
    print('\033[1;31mJogador perdeu!\033[m')

