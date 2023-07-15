words = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Lenda',
         'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador',
         'Futuro')
for p in words:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letters in p:
        if letters.lower() in 'aeiou':
            print(letters, end=' ')
