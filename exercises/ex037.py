#Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
#-1 para binário
#-2 para octal
#3 para hexadecimal

n = int(input('Me diga um número inteiro:'))
base = int(input('Qual base de conversão você quer?\n -1 para Binário \n -2 para Octal \n -3 para Hexadecimal \n Digite aqui:'))
if base == 1:
    binario = bin(n)
    print(f'O número {n} convertido em binário é: {binario}.')
elif base == 2:
    octal = oct(n)
    print(f'O número {n} convertido em octal é: {octal}.')
elif base == 3:
    hexa = hex(n)
    print(f'O número {n} convertido em hexadecimal é: {hexa}.')
else:
    print('Comece novamente, digitando uma das três opções, por favor.')
