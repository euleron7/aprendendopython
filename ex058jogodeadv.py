from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez: ')
        elif jogador > computador:
            print('Menos... Tente denovo: ')
print('Acertou com {} tentativas.'.format(palpites))