#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

x = 0
numeros = []

for x in range(0,5):
    numeros.append((int(input('Insira um número: '))))

for x in range(0,5):
    print(numeros[x])

