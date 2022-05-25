#Faça um programa que leia uma frase pelo teclado e mostre:
#- Quantas vezes aparece a letra "A"
#- Em que posição ela aparece a primeira vez
#- Em que posição ela aparece a última vez


frase = str(input('Digite uma frase qualquer: - ')).upper().strip()
vzs = frase.count('A')
primeiravez = frase.find('A')
ultima = frase.rfind('A')

print(f'A letra A aparece {vzs} vezes.')
print(f'A letra A aparece pela primeira vez na {primeiravez}º posição.')
print(f'A letra A aparece pela última vez na {ultima}º posição.')