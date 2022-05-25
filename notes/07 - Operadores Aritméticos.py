# Adição +
# Subtração -
# Multiplicação *
# Divisão /
# Potência **
# Divisão Inteira //
# Resto da Divisão %

#Ordem de Precedência
#1 - ( )
#2 - **
#3 - * / // %
#4 - + -

#nome =input('Qual é o seu nome')
#print(f'Prazer em te conhecer {nome:^20}')

n1 = int(input('um valor: '))
n2 = int(input('outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}.', end=' ')
print(f'Além disso, a divisão inteira é {di} e a exponenciação é {e}.')