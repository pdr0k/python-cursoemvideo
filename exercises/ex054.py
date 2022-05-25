#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
count1 = 0
count2 = 0
for loop in range(1,8):
    ano = int(input('Que ano você nasceu? - '))
    if ano>2004: #menor
        count1+=1
    if ano<=2004: #maior
        count2+=1

print(f'{count1} pessoas não atingiram a maioridade e {count2} atingiram.')

#Com a data real

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input(f'Em que ano a {pess}ª pessoas nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else: totmenor +=1
print(f'Tivemos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade.')