from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento do alistando: '))
idade = atual - nasc
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE. Apresente-se ao exército o mais breve possível.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos. Apresente-se ao exército para esclarecimentos.'.format(saldo))

#perguntar se é homem ou mulher

