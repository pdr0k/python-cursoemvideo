#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Dê um comprimento de reta: '))
b = float(input('Dê outro comprimento de reta: '))
c = float(input('Dê o último comprimento de reta: '))

if a+b>c and b+c>a and a+c>b:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')