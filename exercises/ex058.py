#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
#foram necessários para vencer.

#028 -
##Escreva um programa que faça um computador "pensar" em
# um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

list = [0,1,2,3,4,5,6,7,8,9,10]
correto = (random.choice(list))
escolha = int(input('Dê um palpite entre 0 e 10: '))
palpite = 1
while escolha != correto:
    escolha = int(input('Você errou! Tente novamente: '))
    if escolha != correto:
        palpite += 1
    else:
        palpite += 1
print(f'Você acertou depois de {palpite} palpites! O número era {correto}.')

outra forma:

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!.')