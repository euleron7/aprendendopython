frase = str(input('Digite uma frase ou uma palavra: ')).strip().upper()
palavras = frase.split()
tdjunto = ''.join(palavras)
inverso = ''
for letra in range(len(tdjunto) - 1, -1, -1):
    inverso += tdjunto[letra]
print('{} ao contrário fica: {}'.format(frase, inverso))
if inverso == tdjunto:
    print('Isso é um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo.')


