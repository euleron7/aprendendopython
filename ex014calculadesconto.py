produto = float(input('Quanto custa o produto? R$'))
desc = produto - (produto * 5 / 100)

print('Este produto de R${:.2f} com o novo desconto ficará R${:.2f}'.format(produto, desc))