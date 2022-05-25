#Elabore um programa que calcule o valro a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros.

preco = float(input('Qual é o preço do produto? '))
vista = str(input('Você irá pagar a vista? ')).upper()
if vista=='SIM':
    metodo = str(input('Qual o método de pagamento?')).upper()
    if metodo == 'DINHEIRO' or metodo == 'CHEQUE':
        print(f'O preço do produto ficará: R${preco*0.9:.2f}.')
    elif metodo == 'CARTAO':
        print(f'O preço do produto ficará: R${preco*0.95:.2f}.')
else:
    cartao = int(input('Em quantas vezes no cartão? '))
    if 1<=cartao<=2:
        print(f'O preço do produto ficará: R${preco:.2f}.')
    else:
        print(f'O preço do produto ficará: R${preco*1.2:.2f}')

