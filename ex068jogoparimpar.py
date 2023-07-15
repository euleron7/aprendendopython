from random import randint
v = 0
while True:
    paroimpar = str(input('Você vai jogar PAR ou ÍMPAR? [P / I]: ')).upper().strip()[0]
    maquina = randint(0,10)
    numero = int(input('Qual número você quer jogar?: '))
    total = maquina + numero
    print('=-' * 25)
    print(f'A máquina jogou {maquina} e você {numero}. O total é {total}.')
    print('Deu PAR!' if total % 2 == 0 else 'Deu ÍMPAR')
    print('=-' * 25)
    if paroimpar == 'P':
        print('Você escolheu PAR.')
        if total % 2 == 0:
            print('Você ganhou.')
            v += 1
        else:
            print('Você perdeu.')
            break
    if paroimpar == 'I':
        print('Você escolheu Ímpar.')
        if total % 2 == 1:
            print('Você ganhou.')
            v += 1
        else:
            print('Você perdeu.')
            break
print(f'GAME OVER! Você venceu {v} vezes.')

