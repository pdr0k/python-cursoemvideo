#Crie um programa que leia dois valores e mostre um menu na tabela.
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
menu = 0
while menu != 5:
    menu = int(input('''
    O que você quer fazer agora?
    [1] Somar os números
    [2] Multiplicar os números
    [3] Descobrir qual é o maior número
    [4] Digitar outros números
    [5] Sair do programa
    E aí? - '''))
    if menu == 1:
        soma = n1 + n2
        print(f'A soma dos números é {soma}.')
    if menu == 2:
        x = n1*n2
        print(f'A multiplicação dos números é {x}')
    if menu == 3:
        if n1>n2:
            print(f'{n1} é o maior.')
        elif n2>n1:
            print(f'{n2} é o maior.')
        else:
            print('Os valores são iguais.')
    if menu == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
print('Programa encerrado.')
    


