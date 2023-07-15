from random import choice

Objetivo1 = 'Parar os habitantes monstruosos da masmorra de atacar o mundo da superfície.'
Objetivo2 = 'Frustrar a trama de um vilão maligno.'
Objetivo3 = 'Destruir uma ameaça mágica dentro de uma masmorra.'
ListaObjetivo = [Objetivo1, Objetivo2, Objetivo3]
ObjetivoAtual = choice(ListaObjetivo)
print('O Objetivo da missão é {}'.format(ObjetivoAtual))

Vilao1 = 'Besta ou monstruosidade sem motivações específicas'
Vilao2 = 'Aberração propensa a corrupção ou dominação'
Vilao3 = 'Corruptor propenso a corrupção ou destruição'
ListaVilao = [Vilao1, Vilao2, Vilao3]
VilaoAtual = choice(ListaVilao)
print('O vilão da missão é um(a) {}'.format(VilaoAtual))

Local1 = 'Catacumbas ou esgotos abaixo de uma cidade'
Local2 = 'Abaixo de uma casa de fazenda'
Local3 = 'Abaixo de um cemitério'
ListaLocal = [Local1, Local2, Local3]
LocalMissao = choice(ListaLocal)
print('O local da missão é {}'.format(LocalMissao))