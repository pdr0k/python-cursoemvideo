#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.



n = int(input('Diga um número inteiro: - '))

if n%2 >= 1:
    print(f'{n} é ímpar.')
else:
    print(f'{n} é par.')