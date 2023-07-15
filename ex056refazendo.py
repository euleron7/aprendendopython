mediaidade = 0
nomehomemvelho = ''
totteen = 0
homemmaior = 0
somaidade = 0
print('\033[1:36m=-\033[m' * 15)
print('\033[1:32mAnalisador de Dados\033[m')
print('\033[1:36m=-\033[m' * 15)

for people in range(1,6):
    print('------- \033[1:35m{}ª Pessoa\033[m -------'.format(people))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if people == 1 and sexo in 'Mm':
        homemmaior = idade
        nomehomemvelho = nome
    if sexo in 'Mm' and idade > homemmaior:
        homemmaior = idade
        nomehomemvelho = nome
    if sexo in 'Ff' and idade < 25:
        totteen += 1
mediaidade = somaidade / 5
print('=-' * 20)
print('A \033[1:36mmédia\033[m de idade das pessoas é \033[1:32m{:.1f} anos\033[m.'.format(mediaidade))
print('O nome do \033[1:36mhomem\033[m mais velho é {} e tem \033[1:32m{} anos\033[m.'.format(nomehomemvelho, homemmaior))
print('Um total de \033[1:35m{} mulheres\033[m com menos de \033[1:35m25 anos\033[m.'.format(totteen))
print('=-' * 20)