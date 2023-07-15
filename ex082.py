lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
for p, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Você digitou os valores {lista}')
print(f'Os valores pares são {pares}')
print(f'Os valores ímpares são {impares}')
