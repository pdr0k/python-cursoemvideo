#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1,250.00, calcule um aumento de 10%.
#Para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário? '))
if salario>1250.00:
    aumento = 1.1*salario - 1250.00
    print(f'Você recebeu um aumento de R${aumento}.')
else:
    aumento = 1.15*salario - salario
    print(f'Você recebeu um aumento de R${aumento}.')
