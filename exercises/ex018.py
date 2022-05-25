#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Fale um ângulo qualquer: -'))
sen = math.sin(ang)
cos = math.cos(ang)
tang = math.tan(ang)

print(f'Angulo dado -> {ang}º')
print(f'sen({ang}º) -> {sen}º')
print(f'cos({ang}º) -> {cos}º')
print(f'tng({ang}º) -> {tang}º')