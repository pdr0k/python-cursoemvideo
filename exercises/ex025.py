#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual o seu nome inteiro? - ')).upper()
print(f'O seu nome contém "Silva"? -', 'SILVA' in nome)
