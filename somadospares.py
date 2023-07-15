soma = 0
cont = 0
cont1 = 0
for c in range(1,7):
    numb = int(input('Digite o {} valor: '.format(c)))
    if numb % 2 == 0:
        soma += numb
        cont += 1
    cont1 += 1
print('Você digitou \033[1:32m{}\033[m números, mas apenas \033[1:32m{}\033[m são PARES, e a soma entre os pares é: \033[1:32m{}\033[m'.format(cont1, cont, soma))
