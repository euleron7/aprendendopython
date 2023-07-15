print('~' * 20)

real = float(input('Quantos reais você tem? R$'))
dolar = real / 4.92
euro = real / 5.31
peso = real / 0.02
libra = real / 6.18
print('Com seus R${:.2f} você consegue comprar \nU${:.2f} (Dólar)'.format(real, dolar))
print('€${:.2f} (euros)'.format(euro))
print('${:.2f} (pesos argentinos)'.format(peso))
print('£${:.2f} (Libras esterlinas)'.format(libra))



print('~' * 20)

