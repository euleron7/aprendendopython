print('=-' * 25)
print('\033[1:32mSequência de Fibonnaci!!\033[m')
print('=-' * 25)
primeiro = int(input('Digite quantos termos você quer mostrar: '))
operador1 = 0
operador2 = 1
print('~~' * 25)
print('{} >>> {} '.format(operador1, operador2), end='')
contador = 3
while contador <= primeiro:
    operador3 = operador1 + operador2
    print('>>> {} '.format(operador3), end='')
    operador1 = operador2 #fazendo o t1,t2 e t3 andar p frente
    operador2 = operador3
    contador += 1


