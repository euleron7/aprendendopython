novo = ' '
total = 0
acimademil = 0
menor = 0
while novo != 'N':
    produto = str(input('Nome do produto: '))
    preço = float(input('R$'))
    novo = str(input('Registrar novo produto? [S/N]: ')).strip().upper()[0]
    if menor < preço:
        menor = preço
    if preço < menor:
        menor = preço
    if preço > 1000:
        acimademil += 1
    total += preço
print(f'O valor total da compra foi R${total:.2f}')
print(f'Temos {acimademil} produtos acima de R$1.000 ')
print(f'O menor preço foi de {menor} reais')


