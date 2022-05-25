##Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Exemplo: Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#MANEIRA MATEMÁTICA
n = int(input('Diga um número: - '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'A unidade é {u}')
print(f'A dezena  é {d}')
print(f'A centena é {c}')
print(f'O milhar é {m}')