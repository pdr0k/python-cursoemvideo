# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n0 = str(input('Olá, estudante. Qual é o seu nome? '))
n1 = float(input('Qual foi a sua primeira nota? '))
n2 = float(input('Qual foi a sua segunda nota? '))
m = (n1 + n2) / 2
print(f'Parabéns, {n0}! A sua média é {m}.')