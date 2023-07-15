from datetime import date
ano = int(input('Ano de nascimento do Indicado: '))
hoje = date.today().year
idade = hoje - ano
if idade <= 11:
    print('Com {} anos, você ainda não está pronto para se tornar um DeMolay.'.format(idade))
elif idade >= 12 and idade < 17:
    print('Com {} anos, você já pode se tornar um DeMolay.'.format(idade))
elif idade >= 17 and idade < 19:
    print('Com {} anos, você pode se tornar um DeMolay e tem idade o suficiente para conquistar o grau cavaleiro.'.format(idade))
elif idade >= 19 and idade < 21:
    print('Com {} anos, você pode ser tornar um DeMolay e já tem idade o suficiente para conquistar o grau ébano.'.format(idade))
elif idade >= 21:
    print('Com {} anos, ou você já é um Senior DeMolay ou você não pode mais se tornar um.'.format(idade))

