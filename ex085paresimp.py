numeros = list()

for c in range(0,7):
    numeros.append(int(input(f'Digite o {c+1}º número: ')))
numeros.sort()
print('Números pares: ', end='')
for p in numeros:
    if p % 2 == 0:
        print(p, end=' ')
print()
print('Números ímpares: ', end='')
for p in numeros:
    if p % 2 == 1:
        print(p, end=' ')
print()
print(numeros)