#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar:
#- Valor da casa;
#- Salário do comprador;
#- Em quantos anos ele vai pagar;

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


valor_casa = float(input('Qual o valor da sua casa?'))
salario = float(input('Qual é o seu salário?'))
anos = int(input('Em quantos anos você vai pagar?'))
prestacao_mensal = valor_casa/anos
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será R${prestacao_mensal:.2f}')
if prestacao_mensal <= 0.3*salario:
    print('Seu empréstimo está aprovado')
else:
    print('Seu empréstimo foi negado')