peso = float(input('Peso do paciente em KG: '))
altura = float(input('Altura do paciente em metros: '))
IMC = peso / (altura ** 2)
print('O seu Índice de Massa Corpórea (IMC) é {:.1f}.'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do seu peso ideal.')
elif 18.5 <= IMC < 25:
    print('Você está no seu peso ideal.')
elif  25 <= IMC < 30:
    print('Você está com sobrepeso.')
elif 30 <= IMC < 40:
    print('Você está com Obesidade.')
else:
    print('Você está com obesidade MÓRBIDA. Cuidado! Sua vida pode estar em risco.')
