lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Túplas são imutáveis.
#Não consigo atribuir valores a tupla, a não ser na declaração dela.
for c in range(0, len(lanche)): #ou >> for c in lanche: print(f'eu vou comer {c}')
    print(f'Eu vou comer {lanche[c]}')

ou

for posiç, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posiç}')

print(sorted(lanche))