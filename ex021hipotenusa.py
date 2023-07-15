import math
opo = float(input('Diga o comprimento do cateto oposto: '))
adj = float(input('Diga o comprimento do cateto adjacente: '))
hip = math.hypot(opo, adj)
print('Considerando que o cateto oposto é {}m o cateto adjacente é {}m  o quadrado da hipotenusa é {:.1f}m².'.format(opo, adj, hip))