#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

contadorVogais=0
contadorConsoantes=0

pal = input("Digite uma palavra: ")

palavra = pal.lower()
 
for x in palavra:
    if(x == 'a'or x == 'e'or x == 'i'or x == 'o'or x == 'u'):
        contadorVogais=contadorVogais+1
    else:
        contadorConsoantes=contadorConsoantes+1
 
print(f'A palavra {palavra} contem {contadorConsoantes} consoantes')