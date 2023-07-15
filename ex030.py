fra = str(input('Digita uma frase ')).upper().strip()
print('A letra A aparece {} vezes.'.format(fra.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(fra.find('A')+1))
print('A letra A aparece por último na posição {}'.format(fra.rfind('A')+1))
