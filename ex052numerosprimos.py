num = int(input('Digite um número inteiro: '))
tot = 0
for e in range(1, num + 1):
    if num % e == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')

    print('{}'.format(e), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num,tot))
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo. Lembrando que número primo só é divisível por 1 e por ele mesmo.')


