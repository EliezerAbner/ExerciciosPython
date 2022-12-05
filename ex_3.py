#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
x = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0

for x in range(1,5):
    notas.append(int(input('Insira a nota {}: '.format(x))))

n1,n2,n3,n4 = notas

media = (n1 + n2 + n3 + n4)/4

print('\n')

for x in range(0,4):
    print('Nota {}: {}'.format(x+1,notas[x]))

print('\nMédia: {}'.format(media))
