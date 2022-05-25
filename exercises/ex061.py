#Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

#51
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.


print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA :'))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end ='')
    termo += razao
    cont +=1
print('FIM')
#primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
#razao = int(input('Digite a razão de uma PA: '))
#ultimo = primeiro_termo + (10-1)*razao #Na fórmula, 10 seria o enésimo termo, termo n.
#ultimo = ultimo + 1
#for PA in range(primeiro_termo, ultimo, razao):
#    print(PA, end=' ->')
#print('ACABOU.')
