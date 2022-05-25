#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

city = str(input('Diga o nome de uma cidade: - '))
junto = city.split()
print('A palavra começa com Santo? -', 'SANTO' in junto[0].upper())