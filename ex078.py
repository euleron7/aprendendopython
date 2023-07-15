valores = list()
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont+1}º número: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'O maior valor digitado foi {maior}  e o menor foi {menor}')
print()
for p, v in enumerate(valores):
    if v == maior:
        print(f'O maior número está na posição {p+1}.')
    if v == menor:
        print(f'O menor número está na posição {p+1}.')
'v'



