galera = list()
dados = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: '))) #inputar 3 pessoas
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) #colocar em galera uma cópia de dados
    dados.clear() #toda vez que eu adicionar uma pessoa dá clear no dados e adiciona outra e assim sucessivamente

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade com {p[1]} anos.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade e tem {p[1]} anos')
        totmenor += 1

print(f'{totmaior} pessoas são maiores de idade e {totmenor} são menores de idade.')