numeros = list()
for c in range(0,5):
    usuario = int(input('Digite um valor: '))
    if c == 0 or usuario > numeros[-1]: #se for o primeiro valor
        numeros.append(usuario)
    else:
        posição = 0
        while posição < len(numeros): #vai da posição zero até a última posição
            if usuario <= numeros[posição]:
                numeros.insert(posição, usuario)
                break
            posição += 1
print('¨¨' * 30)
print(f'Os valores digitados em ordem foram {numeros}')









