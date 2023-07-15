casa = float(input('Valor da casa que deseja comprar: '))
salario = float(input('Qual seu salário: '))
anos = int(input('Em quantos anos pretende pagar essa casa? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('O valor da prestação ficará R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('Concederemos o empréstimo de R${:.2f} a você para pagar em {} anos. O valor da prestação será R${:.2f}.'.format(casa, anos, prestaçao))
else:
    print('Seu empréstimo foi negado.')