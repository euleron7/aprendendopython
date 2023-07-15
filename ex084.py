pessoas = list()
dados = list()
maior = menor = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0: #se eu não coloquei nennhuma pessoa ainda
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    dados.append(pessoas[:])
    pessoas.clear()
    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
print(f'Você cadastrou {len(dados)} pessoas na plataforma.')
print(f'O maior peso foi {maior}. Pessoas: ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0].capitalize()}]', end='')
print()
print(f'O menor peso foi {menor}. Pessoas:', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0].capitalize()}]', end='')
print()
print(dados)