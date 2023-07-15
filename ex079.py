numeros = list()
while True:
    usuario = int(input('Digite um valor: '))
    if usuario not in numeros:
        numeros.append(usuario)
        print('Valor adicionado')
    else:
        print('Você já digitou esse valor')
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print('¨¨' * 35)
numeros.sort()
print(f'Você digitou os valores {numeros}')
