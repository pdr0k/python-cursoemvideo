#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pessoas in range(1,6):
    peso = float(input(f'Qual é o peso da {pessoas}º pessoa?' ))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso lido foi {maior}Kg e o menor foi {menor}Kg')

