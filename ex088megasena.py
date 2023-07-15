from random import randint
qtd_numeros = 6
max_valor = 61
numeros = []
maisnumeros = []
jogos = int(input('Quantos jogos você quer sortear? '))
print('¨¨' * 20)
print('$$$$$ JOGOS DA MEGA SENA $$$$$')
print('¨¨' * 20)
for c in range(0, jogos):
    numeros = [] # limpa a listas de números para cada jogo
    while len(numeros) < qtd_numeros:
        computador = randint(1, max_valor)
        if computador not in numeros:
            numeros.append(computador)
    numeros.sort()
    print(f'Jogo {c+1}: {numeros}')