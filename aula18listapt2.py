teste = list()
teste.append('Euler')
teste.append(25)
galera = list()
galera.append(teste[:]) #adicionar dentro de galera uma cópia de teste
teste[0] = 'Leron'
teste[1] = 35
galera.append(teste)
print(galera)
galera2 = [['joao', 25], ['felas', 13], ['jonatas', 27]] #varias listas dentro de uma lista
print(galera2)
print(galera2[2][0])
print('¨¨' * 30)
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')
