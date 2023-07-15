from random import randint
computador = randint(1,10)
contadorerros = 0
acertou = False
while not acertou:
    jogador = int(input('Digite o seu palpite: '))
    if jogador == computador:
        acertou = True
    else:
        contadorerros += 1
        if jogador > computador:
            print('Você errou, tente um número menor: ')
        if jogador < computador:
            print('Você errou, tente um número maior: ')
print('Você acertou com {} tentativas.'.format(contadorerros))
