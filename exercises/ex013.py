#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

name = str(input('Olá! Qual o seu nome? - '))
salario = float(input(f'Tudo certo contigo, {name}? Me passa o seu salário, para que eu possa verificar o seu aumento: '))
aumento = 1.15*salario

print(f'Então, {name}. O seu salário, com um aumento de 15%, fica R${aumento:.2f}.')
