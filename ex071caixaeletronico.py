saque = int(input('Digite o valor a ser sacado: R$ '))
ced50 = ced20 = ced10 = ced1 = 0
total = 1
total *= saque
while True:
    if saque >= 50:
        ced50 += 1
        saque -= 50
    elif saque >= 20:
        ced20 += 1
        saque -= 20
    elif saque >= 10:
        ced10 += 1
        saque -= 10
    else:
        ced1 += 1
        saque -= 1
    if saque == 0:
        break
print(f'''Serão {ced50} cédulas de R$50,00,
{ced20} cédulas de R$20,00
{ced10} cédulas de 10 reais
{ced1} cédulas de 1 real
Totalizando R${total}.''')