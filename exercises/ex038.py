#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo mvalor é maior
#- Não existe valor maior, os dois são iguais


a = int(input('Digite o 1º número inteiro:'))
b = int(input('Digite o 2º número inteiro:'))
if a>b:
    print(f'{a} é maior que {b}.')
elif b>a:
    print(f'{b} é maior {a}.')
else:
    print('Os números são iguais.')


