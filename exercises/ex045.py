#Crie um programa que faça o computador jogar Jokenpô com você.
import random
vc = str(input('Pedra, Papel, Tesoura! O que você escolheu?')).upper()
lista = ['PEDRA','PAPEL','TESOURA']
bot = random.choice(lista)
if vc == bot:
    print(f'Empatou! Minha escolha foi {bot.capitalize()}.')
if vc == 'PEDRA' and bot == 'PAPEL':
    print(f'Hahahaha, ganhei. Minha escolha foi {bot.capitalize()}.')
elif vc == 'PEDRA' and bot == 'TESOURA':
    print(f'Droga, você ganhou! Minha escolha foi {bot.capitalize()}.')
if vc == 'TESOURA' and bot == 'PAPEL':
    print(f'Droga, você ganhou! Minha escolha foi {bot.capitalize()}.')
elif vc == 'TESOURA' and bot == 'PEDRA':
    print(f'Hahahaha, ganhei. Minha escolha foi {bot.capitalize()}.')
if vc == 'PAPEL' and bot == 'TESOURA':
    print(f'Hahahaha, ganhei. Minha escolha foi {bot.capitalize()}.')
elif vc == 'PAPEL' and bot == 'PEDRA':
    print(f'Droga, você ganhou! Minha escolha foi {bot.capitalize()}.')










