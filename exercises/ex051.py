#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão de uma PA: '))
ultimo = primeiro_termo + (10-1)*razao #Na fórmula, 10 seria o enésimo termo, termo n.
ultimo = ultimo + 1
for PA in range(primeiro_termo, ultimo, razao):
    print(PA, end=' ->')
print('ACABOU.')

