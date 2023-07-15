soma = 0
contador = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        contador += + 1
        soma += + cont
print('A soma de todos os {} os valores solicitados é: \033[1:32m{}\033[m'.format(contador, soma))