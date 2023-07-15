usuario = str(input('Digite a expressão: '))
lista = list()
for letra in usuario: #para cada caractér do que for digitado em usuario, pega cada letra da string q vier em usuario
    if letra == '(':
        lista.append('(') #adicionando o parenteses abrindo na lista
    elif letra == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break           #sinalizando q len de pilha tem 1 então dando n válida, expressão começa com parenteses fechado
if len(lista) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')

