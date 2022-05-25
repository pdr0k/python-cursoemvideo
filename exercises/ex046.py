#Faça um programa que mostre na tela uma contagem regressiva para os fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Os fogos irão começar em:')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Fogos!')
