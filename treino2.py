primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
op1 = primeiro
denovo = 10
tudo = 0
while denovo != 0:
    tudo += denovo
    while contador <= tudo:
        print('{} >>>  '.format(op1),end='')
        op1 += razao
        contador += 1
    denovo = int(input('Quer mostrar mais termos? Digite quantos: '))

print('Fim')
