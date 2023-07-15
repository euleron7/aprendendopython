usuario = tudo = contador = upper = lower = 0
while usuario != 'N':
    numero = int(input('Digite um número: '))
    contador += 1
    tudo += numero
    if contador == 1:
        upper = lower = numero
    else:
        if numero > upper:
            upper = numero
        if numero < lower:
            lower = numero
    usuario = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = tudo / contador
print('Você digitou {} números e a média entre eles foi {}.'.format(contador, media))
print('O maior número digitado foi {} e o menor foi {}'.format(upper, lower))

