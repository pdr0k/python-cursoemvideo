#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: - '))
n2 = float(input('Digite outro número: - '))
n3 = float(input('Digite o último número: - '))

if n1>n2>n3:
    print(f'{n1} é o maior número e {n3} é o menor.')
if n1>n3>n2:
    print(f'{n1} é o maior número e {n2} é o menor.')
if n2>n1>n3:
    print(f'{n2} é o maior número e {n3} é o menor.')
if n2>n3>n1:
    print(f'{n2} é o maior número e {n1} é o menor.')
if n3>n2>n1:
    print(f'{n3} é o maior número e {n1} é o menor.')
if n3>n1>n2:
    print(f'{n3} é o maior número e {n2} é o menor.')
if n1==n2==n3:
    print(f'Todos são iguais.')


