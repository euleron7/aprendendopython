usuario = contador = tudo = 0
usuario = int(input('Digite um número [999 para parar]: '))
while usuario != 999:
    tudo += usuario
    contador += 1
    usuario = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números. A soma dos valores foi: {}'.format(contador, tudo))
