#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for loop in range(1,7):
    n = int(input('Digite um número inteiro:'))
    if n%2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} números pares e a soma destes é {soma}.')



