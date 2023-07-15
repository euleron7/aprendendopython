print('__' * 20)
print('\033[1:32mSobradinho Materiais para Construção e Madeiras.\033[m')
print('__' * 20)
preço = float(input('Valor do produto: '))
print('=-' * 20)
print("""Como será a forma de pagamento:
[1] À vista: 10% de desconto (Dinheiro / Cheque).
[2] Em até 2x no cartão: Preço normal.
[3] À vista no cartão: 5% de desconto.
[4] 3x ou mais no cartão: 20% de juros.""")
print('=-' * 20)
escolha = int(input('Digite a opção desejada: '))
if escolha == 1:
    desc = (10 / 100) * preço
    novo = preço - desc
    print('O preço à vista com 10% de desconto passa de R${} para \033[1:32mR${:.2f}\033[m.'.format(preço, novo))
elif escolha == 2:
    print('Em até 2x no cartão o preço se mantém \033[1:32mR${}\033[m.'.format(preço))
elif escolha == 3:
    desc = (5 / 100) * preço
    novo = preço - desc
    print('À vista no cartão você tem 5% de desconto, passando de R${} para \033[1:32mR${}\033[m.'.format(preço, novo))
elif escolha == 4:
    acresc = (20 / 100) * preço
    novo = preço + acresc
    totparc = int(input('Quantas parcelas: '))
    print('Parcelando o produto em {}x no cartão, terá um acréscimo de 20% na sua compra, ficando no valor de \033[1:32mR${}\033[m.'.format(totparc, novo))
else:
    print('Opção de pagamento inválida. Tente novamente!')
