t1 = float(input('Primeiro segmento de reta: '))
t2 = float(input('Segundo segmento de reta: '))
t3 = float(input('Terceiro segmento de reta: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('=-' * 25)
    print('\033[1:32mOs segmentos PODEM formar um triângulo.\033[m')
    print('=-' *25)
    if t1 == t2 == t3:
        print('Esse triângulo é um triângulo \033[1:36mequilátero\033[m.')
    elif t1 == t2 or t1 == t3 or t2 == t1 or t2 == t3 or t3 == t1 or t3 == t2:
        print('Esse triângulo é um triângulo \033[1:36misósceles\033[m.')
    else:
        print('Esse triângulo é um triângulo \033[1:36mescaleno\033[m.')
else:
    print('=-' * 25)
    print('\033[1:31mOs segmentos NÃO PODEM formar um triângulo.\033[m')
    print('=-' * 25)