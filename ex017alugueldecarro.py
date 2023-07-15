dias = int(input('Quantos dias foram o aluguel do carro?: '))
km = float(input('Quantos quilômetros foram percorridos? Km: '))
valor = (dias * 60) + (km * 0.15)
print('O valor total a se pagar pelo aluguel do carro é de R${:.2f}.'.format(valor))