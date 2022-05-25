#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo, sem considerar espaços
# - Quantas letras tem o primeiro nome


nome = str(input('Olá, seja bem vindo. Qual é o seu nome inteiro? '))
print(f'O seu nome com todas as letras maiúsculas fica: {nome.upper()}')
print(f'O seu nome com todas as letras minúsculas fica: {nome.lower()}')
div = nome.split()
junto = ''.join(div)
print(f'No total, sem considerar espaços, seu nome tem {len(junto)} letras. ')
print(f'Seu primeiro nome tem {len(div[0])} letras.')




