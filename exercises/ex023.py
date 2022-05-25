#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Exemplo: Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1


n = str(input('Digite um número de 0 a 9999: - '))
uni = n[3]
dez = n[2]
cen = n[1]
mil = n[0]
print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')

#essa solução tem o problema dos quatro digitos