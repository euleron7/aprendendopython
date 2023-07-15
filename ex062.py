print('Gerador de PA')
print('=-' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
op1 = primeiro
contador = 1
tudo = 0
denovo = 10
while denovo != 0:
    tudo += denovo
    while contador <= tudo:
        print('{} >>> '.format(op1), end='')
        op1 += razao
        contador += 1
    print('Pausa')
    denovo = int(input('Quer mostrar mais termos? Digite quantos: '))
print('Fim')
print('Progressão finalizada com {} termos.'.format(tudo))