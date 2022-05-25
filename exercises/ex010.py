# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

name = str(input('Olá! Qual é o seu nome? - '))
cart = float(input(f'Olá, {name}, tudo bom? Quanto você possui na carteira?'))
dol = cart/3.27
print(f'Então, {name}, com R${cart} na carteira, você consegue adquirir ${dol:.2f}.')