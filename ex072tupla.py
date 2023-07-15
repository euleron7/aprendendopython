numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    usuario = int(input('Digite um número entre 0 e 20: '))
    if 0 <= usuario <= 20:
        print(f'Você digitou o número {numeros[usuario]}')
        continuar = str(input('Você quer continuar? "S" para continuar "N" para sair: ')).strip().upper()[0]
        if continuar == 'N':
            print('Programa encerrado.')
            break
        elif continuar == 'S':
            continue

    else:
        print('Tente novamente.')

