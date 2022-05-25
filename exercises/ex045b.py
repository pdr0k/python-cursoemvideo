#Crie um programa que faça o computador jogar Jokenpô com você.
import random
vc = str(input('Pedra, Papel, Tesoura! O que você escolheu?')).upper()
lista = ['PEDRA','PAPEL','TESOURA']
bot = random.choice(lista)
if vc == 'TESOURA':
    if bot == 'PEDRA':
        print(f'Você perdeu! Escolhi {bot.capitalize()}.')
    elif bot == 'PAPEL':
        print(f'Você ganhou! Escolhi {bot.capitalize()}.')
if vc == 'PAPEL':
    if bot == 'TESOURA':
        print(f'Você perdeu! Escolhi {bot.capitalize()}.')
    elif bot == 'PEDRA':
        print(f'Você ganhou! Escolhi {bot.capitalize()}.')
if vc == 'PEDRA':
    if bot == 'PAPEL':
        print(f'Você perdeu! Escolhi {bot.capitalize()}.')
    elif bot == 'TESOURA':
        print(f'Você ganhou! Escolhi {bot.capitalize()}.')
if vc == bot:
    print(f'Empatou. Escolhi {bot.capitalize()}.')