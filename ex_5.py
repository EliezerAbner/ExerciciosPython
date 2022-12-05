#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

int_num = []
impar = []
par = []

for x in range(0,20):
    int_num.append(x)

while(x<20):
    if int_num[x]%2==0:
        par.append(int_num[x])
    else:
        impar.append(int_num[x])
    
    x = x + 1

print(par)
print(impar)
print(int_num)
