#Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa.
#math.hypot(x, y): Retorna a hipotenusa dos números (catetos) fornecidos.

from math import hypot
print('\nCALCULO DA HIPOTENUSA DE UM TRIANGULO RETANGULO \n')
x = float(input('Digite o valor do cateto oposto (X): '))
y = float(input('Digite o valor do cateto adjacente (Y): '))
print('O valor da hipotenusa (Z) deste triângulo retangulo é: {:.2f} \n' .format(hypot(x,y)))
