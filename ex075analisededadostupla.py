n1 = (int(input('Digite um número: ')),
      int(input('Digite o segundo número: ')),
      int(input('Digite mais um: ')) ,
      int(input('Agora o último número: ')))
print(f'Você digitou os valores {n1}')
print(f'O valor 9 apareceu {n1.count(9)} vezes.')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3)}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for numero in n1:
    if numero % 2 == 0:
        print(numero, end=' ')