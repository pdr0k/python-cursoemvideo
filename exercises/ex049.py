#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que utilizando o laço for.
# 009 -Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada
n = int(input('Diga um número inteiro: '))
print(f'A tabuada de {n} é:')
for tabuada in range(1,11):
    print(f'{n} x {tabuada} = {n*tabuada}')