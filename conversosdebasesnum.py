numb = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opc =  int(input('Qual sua opção: '))
if opc == 1:
    print('O número {} convertido para binário é {}.'.format(numb, bin(numb)[2:]))
elif opc == 2:
    print('O número {} convertido para octal é {}.'.format(numb, oct(numb)[2:]))
elif opc == 3:
    print('O númer {} convertido para hexadecimal é {}.'.format(numb, hex(numb)[2:]))
else:
    print('Opção inválida, animal, tente novamente.')