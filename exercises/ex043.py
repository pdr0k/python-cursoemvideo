#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# Acimade 40: Obesidade mórbida

peso = float(input('Qual é o seu peso em kg?'))
altura = float(input('Qual é sua altura em metros?'))
imc = peso/altura**2
if imc<18.5:
    print('Abaixo do Peso.')
elif 18.5<=imc<25:
    print('Peso Ideal.')
elif 25<=imc<30:
    print('Sobrepeso.')
elif 30<=imc<40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')