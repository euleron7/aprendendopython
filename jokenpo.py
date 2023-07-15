from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print("""Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura""")
jogador = int(input('O que você vai jogar? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
print('O computador escolheu: {}'.format(itens[computador]))
print('O jogador escolheu: {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Você perdeu!')
elif computador == 1:
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Você ganhou!')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('EMPATE!')