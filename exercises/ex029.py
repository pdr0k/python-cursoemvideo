# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada KM acima do limite.


vm = float(input('Qual a velocidade do seu carro? - '))
if vm>80:
    multa = (vm-80)*7
    print(f'Você foi multado em: R${multa:.2f}.')
print('Tenha um bom dia, dirija com segurança.')
