somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulherteen = 0
for p in range(1, 6):
    print('________{}ª PESSOA________'.format(p))
    nome = str(input('Nome da pessoa: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulherteen += 1

mediaidade = somaidade / 5
print('A média da idade das pessoas é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Um total de {} mulher com menos de 20 anos.'.format(totmulherteen))
