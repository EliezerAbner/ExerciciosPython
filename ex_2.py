#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

x = 0
numeros = []

for x in range(0,10):
    numeros.append(x)

numeros.reverse()

for x in range(0,10):
    print(numeros[x])