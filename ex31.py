nome = str(input('Digite o seu nome completo: '))
split = nome.split()
print('Seu primeiro nome é {}'.format(split[0]))
print('Seu último nome é {}'.format(split[len(split)-1]))