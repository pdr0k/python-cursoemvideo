# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

name = str(input('Olá, tudo jóia? Qual o seu nome? - '))
larg = float(input(f'Bom ter você por aqui, {name}. Qual é a largura da sua parede, em metros? - '))
alt = float(input('Ah, entendi. E a altura, em metros? - '))
a = larg * alt
qnt = a/2
print(f'Bom, {name}. A sua parede tem uma área de {a:.2f}m^2, então serão necessários {qnt:.2f} litros de tinta.')