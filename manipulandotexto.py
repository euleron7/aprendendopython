texto = """Tô no páreo, caralho, fumando droga
É o rap carioca chegando tocando o zaralho
Quem reclamar vai perder
Se o mundo não te entendeu, cê não se fez entender
Atrás da glória, trampando o dia inteiro
Na prática, a vitória é de quem pega primeiro
Sou tiro que arranca máscara
Meu partido sou eu tipo Hezbollah
Tô no TTK, manda vir me pegar
Seu respeito já não basta, só seu medo bastará"""

print(texto.replace('glória', 'xota'))
print('glória' in texto)
print(texto.find('ó'))
print(texto.lower().find('atrás'))
dividido = texto.split()
print(dividido[28])
print(dividido[28][3])



