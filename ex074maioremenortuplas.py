from random import randint
contador = upper = lower = 0
numbersaleatorios = ()
for c in range(5):
    computador = randint(1,100)
    contador += 1
    numbersaleatorios += (computador,)
    if contador == 1:
        upper = lower = computador
    else:
        if computador > upper:
            upper = computador
        if computador < lower:
            lower = computador
print(f'\033[1:32m{numbersaleatorios}\033[m são os números que foram sorteados pela máquina.')
print(f'O maior valor da Tupla é o \033[1:31m{upper}\033[m e o menor valor da Tupla é o \033[1:34 m{lower}\033[m')

