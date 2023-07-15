import math
angulo = float(input('digite o angulo que você deseja '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('O angulo de {:.2f} graus representa \n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(angulo, seno, cos, tg))