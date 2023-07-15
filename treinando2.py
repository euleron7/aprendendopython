cidade = str(input('Vamos descobrir se a sua cidade tem santo no nome, digite o nome da sua cidade: ')).strip().upper()
split = cidade.split()
print('SANTO' in cidade)