#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Diga um número: '))
nn = 2 * n
nnn = 3 * n
rn = n**(1/2)
print(f'O número dito foi {n}.')
print(f'Seu dobro é {nn} e seu triplo é {nnn}.')
print(f'Para finalizar, sua raiz quadrada é {rn}.')
