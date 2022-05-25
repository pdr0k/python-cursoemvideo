##Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Pode ser feito de uma maneira diferente também.

a = float(input('Digite um número: - '))
b = float(input('Digite outro número: - '))
c = float(input('Digite o último número: - '))
#Quem é o menor
menor = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#Quem é o maior

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior número é {maior} e o menor é {menor}')