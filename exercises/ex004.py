#2 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

alg = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(alg))
print('Só tem espaços? ', alg.isspace())
print('É um número? ', alg.isnumeric())
print('É alfabético? ', alg.isalpha())
print('É alfanumérico? ', alg.isalnum())
print('Está em maiúsculas? ',alg.isupper())
print('Está em minúsculas? ', alg.islower())
print('Está capitalizada? ',alg.istitle())
