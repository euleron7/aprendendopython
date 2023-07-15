from random import randint
computador = randint(1,10)
acertou = False
contadorerros = 0
while not acertou:
    jogador = int(input('Duvido você advinhar em qual número eu pensei: '))
    if jogador == computador:
        acertou = True
    else:
        contadorerros += 1
        if computador > jogador:
            print('Você errou, tente um número maior: ')
        if computador < jogador:
            print('Você erroum tente um número menor: ')
print('Eu pensei no número \033[1:32m{}\033[m'.format(computador))
print('Parabéns!! Você acertou com {} tentativas.'.format(contadorerros))