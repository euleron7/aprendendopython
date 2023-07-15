while True:
    tabuada = int(input('Quer saber a tabuada de qual número: '))
    if tabuada < 0:
        print('Programa encerrado.')
        break
    contador = 1
    while contador <= 10:
        result = tabuada * contador
        print(f'{tabuada} x {contador} = {result}')
        contador += 1
