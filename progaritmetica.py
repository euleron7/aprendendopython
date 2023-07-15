termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo + (20 - 1) * razao
for e in range(termo, decimo + razao, razao):
    print('{}'.format(e), end=' → ')
print('FIM!')