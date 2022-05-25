#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200km e R$0.45 para viagens mais longas.
#abaixo levando em conta de que até 200km é preço fixo de 100
#km = float(input('Qual a distância da viagem em KM? - '))
#if km<=200:
  #  menor = 0.50*km
  #  print(f'O valor da passagem ficou: R${menor:.2f}.')
#else:
  #  maior = (km-200)*0.45 + 100
  #  print(f'O valor da passagem ficou: R${maior:.2f}.')

#Se o preço for verdadeiramente 0.45 fixo para viagens acima de 200 ficará
distancia = float(input('Qual a distância da viagem em KM? - '))
if distancia<=200:
      preco = distancia * 0.50
else:
    preco = distancia*0.45
print(f'O valor da viagem ficou em: R${preco:.2f}')

