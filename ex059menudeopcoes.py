from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Escolher novos números
    [5] Saior do programa''')
    sleep(0.3)
    print('=-' * 20)
    opcao = int(input('Qual sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))

    elif opcao == 2:
        multiplicador = n1 * n2
        print('{} x {} é {}.'.format(n1, n2, multiplicador))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é: {}.'.format(n1, n2, maior))

    elif opcao == 4:
        print('Informe os números novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-' * 20)
    sleep(2.3)