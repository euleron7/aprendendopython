n1 = float(input('Nota 1 do Aluno: '))
n2 = float(input('Nota 2 do Aluno: '))
media = (n1 + n2) / 2
if media < 7 and media >= 5:
    print('O aluno está de recuperação: ')
elif media < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')