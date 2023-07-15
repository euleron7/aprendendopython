numero = soma = contador = 0
while True:
    numero = int(input('Digite um número(Digite 999 para parar): '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Você digitou {contador} números e a soma entre eles foi {soma}!')