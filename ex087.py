matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('¨¨' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

    print()
print(f'A soma dos valores pares é: {spar}')
for l in range(0, 3):
    scoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {scoluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')