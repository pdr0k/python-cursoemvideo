#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no
#final do jogo.


import random

count = 0
print('-='*30)
print('Par ou ímpar')
print('-='*30)
while True:
    n = int(input('Escolha um número de zero a dez - '))
    user_choice = str(input('Par ou Ímpar? [P/I] - ')).strip().upper()[0]
    print('-='*30)
    bot_list = [0,1,2,3,4,5,6,7,8,9,10]
    bot_choice = (random.choice(bot_list))
    result = n + bot_choice
    par_impar = 0
    if result %2 == 0:
        par_impar = 'PAR'
    else:
        par_impar = 'ÍMPAR'
    if (result %2 == 0 and user_choice == 'P' or result %2 != 0 and user_choice == 'I'):
        count += 1
        print(f'Você escolheu {n} e o computador {bot_choice}. O total foi {result}, {par_impar}!')
        print('Você ganhou!')
        print('Vamos jogar de novo...')
        print('-='*30)
        continue
    else:
        print(f'Você escolheu {n} e o computador {bot_choice}. O total foi {result}, {par_impar}!')
        print(f'Você perdeu depois de ter vencido {count} vezes.')
        print('Game Over!')
        break
print('Programa Encerrado')




#poderia ser utilizado randint(0,10), evitando a criação da lista
#utilizei a instrução continue mesmo o guanabara não tendo ensinado, pois no site sololearn aprendi como funciona
