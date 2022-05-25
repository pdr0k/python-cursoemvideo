# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math

real = float(input('Me diga um número real: - '))
print(f'A porção inteira do número {real} é {math.trunc(real)}')