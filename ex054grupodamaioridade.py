from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for pessoas in range(1, 8):
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print('Das {} pessoas listadas {} são MAIORES e {} são MENORES.'.format(pessoas, maiores, menores))
