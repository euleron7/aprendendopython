lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120,
         'Canetas', 22.30,
         'Livro', 34.90)
for posição in range(0, len(lista)):
    if posição % 2 == 0:
        print(f'{lista[posição]:.<30}', end='')
    else:
        print(f'R${lista[posição]:>7.2f}')
print(len(lista))