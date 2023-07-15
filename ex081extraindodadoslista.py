contador = 0
lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    contador += 1
    if continuar in 'Nn':
        break
print(f'Você digitou {contador} valores.')
print(f'{lista}')
lista.sort(reverse=True)
print(f'Os valores que você digitou em ordem decrescente é: {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')
