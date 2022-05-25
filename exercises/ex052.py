#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Diga um número inteiro:'))
mult = 0
for count in range(2,n+1):
    if n%count ==0 :
        print(f'{n} não é um número primo, sendo múltiplo de {count} ')
        mult +=1
if mult == 0:
        print(f'{n} é primo.')
else:
        print(f'Tem {mult} múltiplos acima de 2 e abaixo de {n}')



