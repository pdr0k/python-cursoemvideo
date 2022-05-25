#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

name = str(input('Olá! Qual é o seu nome? - '))
price = float(input(f'Tudo bem, {name}? Qual é o preço do produto que deseja verificar o desconto? - '))
dsct = price*0.95
print(f'Então, {name}. Verifiquei aqui e o seu produto, com desconto, sai por R${dsct:.2f}.')