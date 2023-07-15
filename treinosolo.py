preco = float(input('Quanto custa o produto? R$'))
avista = preco - (preco * 10 / 100)
aprazo = preco + (preco * 6 / 100)
print('O produto atualmente custa R${:.2f}.'.format(preco))
print('Se você pagar à vista ganhará um desconto de 10%, ficando no valor de R${:.2f}.'.format(avista))
print('Mas se optar por parcelar nós parcelamos, mas terá um acréscimo de 6%, ficando no valor de R${:.2f}.'.format(aprazo))
print('Parcelamos em até 12x no cartão!')

