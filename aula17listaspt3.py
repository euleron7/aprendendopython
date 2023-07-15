a = [7, 5, 3, 4, 0]
b = a[:] #cria uma cópia da lista, assim b não tem ligação com a, sem o [:] a variável seria ligada uma na outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')