#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.

#Calcule e mostre o comprimento da hipotenusa.

import math

sen = float(input('Qual é o cateto oposto do triângulo? - '))
cos = float(input('Qual é o cateto adjacente do triângulo? - '))

print(f'A hipotenusa é {math.hypot(sen,cos)}.')
