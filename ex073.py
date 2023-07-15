times = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Bragantino', 'Fluminense',
         'São Paulo', 'Internacional', 'Atlético-PR', 'Atlético-MG', 'Fortaleza',
         'Cruzeiro', 'Cuiabá', 'Santos', 'Bahia', 'Corinthians', 'Goiás', 'Vasco da gama', 'América-MG', 'Coritiba')
print('Classificação Brasileirão 2023')
print(f'{times}')
print('-*' * 20)
print(f'Os cinco primeiros times são {times[0:5]}')
print('-*' * 20)
print(f'Os times que estão no G4: {times[-4:]}')
print('-*' * 20)
print(f'Ordem alfabética: {sorted(times)}')
print('-*' * 20)
print(f'O Palmeiras está na {times.index("Palmeiras") + 1}ª posição')