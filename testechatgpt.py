import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de Adivinhe o Número!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    while True:
        tentativa = int(input("Digite um número: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior!")
        elif tentativa > numero_secreto:
            print("Tente um número menor!")
        else:
            print("Parabéns! Você acertou o número em", tentativas, "tentativas!")
            break

    print("Obrigado por jogar!")

jogar_adivinhacao()