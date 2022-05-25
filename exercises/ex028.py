#Escreva um programa que faça um computador "pensar" em
# um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

list = [0,1,2,3,4,5]
correto = (random.choice(list))
n = int(input('Escolha um número inteiro entre 0 e 5: '))
if n==correto:
    print('Parabéns, você acertou!')
else:
    print('Você perdeu, tente novamente.')


#poderia ser também
#from random import randint
#computador = randint(0,5)