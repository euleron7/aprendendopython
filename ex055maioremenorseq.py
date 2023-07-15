for p in range(1,6):
    peso = float(input('Peso da pessoa: '))
    if p == 1:
        maior = peso                         #já pego o primeiro peso da primeira pessoa e crio duas variáveis com o mesmo valor
        menor = peso
    else:
        if peso > maior:                  #fiz a troca da variável
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi de {}Kg.'.format(menor))