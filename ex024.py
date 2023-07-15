import random
al1 = str(input('Diga o primeiro nome: '))
al2 = str(input('Diga o segundo nome: '))
al3 = str(input('Diga o terceiro nome: '))
al4 = str(input('Diga o quarto nome: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A sequência será: ')
print(lista)
