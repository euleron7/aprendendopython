from random import randint
computador = randint(1,10)
acertou = False
contadorerros = 0
while not acertou:
    jogador = int(input('Dê o seu palpite de 1 a 10: '))
    if jogador == computador:
        acertou = True
    else:
        contadorerros += 1
        if jogador > computador:
            print('Você errou, tem um número menor.')
        if jogador < computador:
            print('Você errou, tente um número maior.')
print('Você acertou com {} tentativas.'.format(contadorerros))