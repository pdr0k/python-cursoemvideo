#Escreva um programa que pergunte a quantidade de Km percorridos pro um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado


kmperc = float(input('Quantos Kms foram percorridos? - '))
diaalug = int(input('Por quantos dias ele foi alugado? - '))

kmf = 0.15 * kmperc
diaf = 60 * diaalug
final = kmf + diaf

print(f'{kmperc} kilômetros em {diaalug} dias dá um preço final de R${final}.')


