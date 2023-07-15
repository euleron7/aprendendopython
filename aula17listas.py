num = ['meu piru', 'meu zovão', 'minha casseta', 'nois q voa bruxas', 'viado', 'viado', 'viado']
num[1] = 'ta porra' #trocando um elemento por outro
print(num)
num.append('cê ta viajano fio') #adicionando elemento
print(num)
num.sort() #organiza os elementos
print(num)
num.sort(reverse=True) #organiza os elementos ao contrário
print(num)
print('==-' * 30)
print(f'Essa lista tem {len(num)} elementos') #contando quantos elementos na lista
num.insert(2, 'meu zovinho') #adicionando (insert) elemento na posição 2
print(num)
num.pop()
print(num) #elimina último elemento
num.pop(2)
print(num) #elimina o elemento 2 (na terceira casa)
num.remove('ta porra') #remove o 'taporra'
print(num)
if 'viado' in num: #remove 'viado'
    num.remove('viado')
else:
    print('não achei "viado" ')
print(num)