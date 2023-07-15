print('Gerador de PA')
print('=-' * 15)
primeiro = int(input('Primeiro termo: '))
final = int(input('Razão da PA: '))
op1 = primeiro
contador = 1
while contador <= 10:
    print('{} >>>> '.format(op1), end='')
    op1 += final
    contador += 1
print('FIM!!')