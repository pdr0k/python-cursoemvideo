#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato.
cart = count_1000 = cheapest = count_products = 0
product_name_cheapest = ''
print('-' * 44)
print('-' * 15, 'LOJINHA ZIKA', '-' * 15)
print('-' * 44)
while True:

    product_name = str(input('Nome do produto: ')).capitalize().strip()
    product_price = float(input('Preço: R$'))
    count_products += 1
    cart += product_price

    if product_price > 1000:
        count_1000 += 1

    if count_products == 1 or product_price < cheapest:
        cheapest = product_price
        product_name_cheapest = product_name

    choice = str(input('Quer continuar? [S/N]')).strip().upper()
    while choice not in 'SN':
        choice = str(input('Quer continuar? [S/N]')).strip().upper()


    if choice == 'N':
        break

print('{:-^44}'.format('FIM DO PROGRAMA'))
print(f'O carrinho de compras está no valor de R${cart:.2f}.')
print(f'{count_1000} produtos custaram mais de R$1000.00')
print(f'O produto mais barato foi {product_name_cheapest} que custa R${cheapest:.2f}')



