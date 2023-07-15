valores = list() #list cria uma lista
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
for posição, valor in enumerate(valores): #o enumerate ele pega tanto a chave quanto o valor
    print(f'Na posição {posição} encontrei  {valor}!')
print('Cheguei ao final da lista')

