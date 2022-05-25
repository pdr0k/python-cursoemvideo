#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
name = str(input(' Qual é o seu nome? '))
obj = str(input(f' Olá, {name}, seja bem-vindo! Qual é o objeto que você quer medir? '))
m = float(input(f' Quantos metros o {obj} possui? '))
cm = m*100
mm = cm*10

print(f'Então, {name}, o {obj} possui {cm:.2f} centímetros e {mm:.2f} milímetros.')
