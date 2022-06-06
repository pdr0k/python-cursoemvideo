#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Qual tabuada de qual valor? - '))
    print('-'*30)
    if n < 0:
        break
    for x in range(1,11):
        tabuada = n*x
        print(f'{n} x {x} = {tabuada}')
    print('-'*30)





print('Programa Encerrado.')