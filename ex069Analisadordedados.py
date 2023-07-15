continuar = ' '
maiores = homens = mulhermenor = 0
while continuar != 'N':
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
print(f'Um total de {maiores} pessoas com mais de 18 anos.')
print(f'Temos um total de {homens} homens cadastrados.')
print(f'Temos um total de {mulhermenor} mulheres com menos de 20 anos.')






