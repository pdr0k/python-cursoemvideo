#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*30)
print('{: ^30}'.format('Banco do Brasil'))
print('='*30)
value = int(input('Qual valor você deseja sacar: R$'))
total = value
note = 50
note_total = 0
while True:
    if total >= note:
        total -= note
        note_total += 1
    else:
        if note_total > 0:
            print(f'Total de {note_total} cédulas de R${note}')
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 1
        note_total = 0
        if total == 0:
            break




