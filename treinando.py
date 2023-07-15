#nome = str(input('Digite o seu nome completo: '))
#split = nome.split()
#print('Seu nome com todas letras maiúsculas é: {}'.format(nome.upper()))
#print('Seu nome com todas letras minúsculas é: {}'.format(nome.lower()))
#print('O seu nome completo tem {} letras.'.format(len(nome.replace(' ', ''))))
#print('O seu primeiro nome tem {} letras.'.format(len(split[0])))


num = int(input('Digite um número de 0 a 9999: '))
string = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))



