import random

def novo_baralho():
    naipes = ['♠', '♣', '♥', '♦']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = [(valor, naipe) for valor in valores for naipe in naipes]
    random.shuffle(baralho)
    return baralho

def valor_carta(carta):
    valor = carta[0]
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)

def contar_pontos(mao):
    total = sum(valor_carta(carta) for carta in mao)
    # Verifica se há Ases na mão e ajusta o valor se necessário
    num_ases = sum(1 for carta in mao if carta[0] == 'A')
    while total > 21 and num_ases > 0:
        total -= 10
        num_ases -= 1
    return total

def jogar_blackjack():
    print("Bem-vindo ao jogo de Blackjack!")
    baralho = novo_baralho()
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_crupie = [baralho.pop(), baralho.pop()]
    while True:
        print("\nSua mão:", mao_jogador, "Total:", contar_pontos(mao_jogador))
        print("Mão do crupiê:", [mao_crupie[0], '?'])
        if contar_pontos(mao_jogador) == 21:
            print("Você tem 21! Você ganhou!")
            break
        elif contar_pontos(mao_jogador) > 21:
            print("Você estourou! Você perdeu!")
            break
        acao = input("O que você quer fazer? (carta/parar): ")
        if acao.lower() == 'carta':
            mao_jogador.append(baralho.pop())
        elif acao.lower() == 'parar':
            while contar_pontos(mao_crupie) < 17:
                mao_crupie.append(baralho.pop())
            print("Mão do crupiê:", mao_crupie, "Total:", contar_pontos(mao_crupie))
            if contar_pontos(mao_crupie) > 21:
                print("O crupiê estourou! Você ganhou!")
            elif contar_pontos(mao_jogador) > contar_pontos(mao_crupie):
                print("Você ganhou!")
            elif contar_pontos(mao_jogador) < contar_pontos(mao_crupie):
                print("Você perdeu!")
            else:
                print("Empate!")
            break

jogar_blackjack()