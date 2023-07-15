while True:
    tabuada = int(input('Quer ver a tabuada de qual valor: '))
    if tabuada < 0:
        print('Programa encerrado')
        break
    contador = 1
    while contador <= 10:
        resultado = tabuada * contador
        print(f'{tabuada} x {contador} = {resultado}')
        contador += 1