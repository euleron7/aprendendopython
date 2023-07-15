for par in range(2, 41):
    if par % 2 == 0:
        print(par, end = ' ' )
print('\033[1:36mEssa foi a contagem dos pares até {}\033[m.'.format(par))