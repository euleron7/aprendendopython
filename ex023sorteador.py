import random
aluno1 = str(input('Qual o primeiro aluno: '))
aluno2 = str(input('Qual o segundo aluno: '))
aluno3 = str(input('Qual o quarto aluno: '))
aluno4 = str(input('Qual o quinto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido é {}'.format(escolhido))




