sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Digite novamente seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
