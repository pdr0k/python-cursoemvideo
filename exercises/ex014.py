#Escreva um programa que converta uma temperatura digitada em c e converta para F
#C para F = X x 1,8 + 32
C = float(input('Digite uma temperatura em ºC - '))
F = (C * 1.8) + 32
print(f'{C}ºC vira {F:.1f}ºF.')
