#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: Junior
#- Até 20 anos: SÊNIOR
#- Acima: MASTER

nasc = int(input('Em que ano você nasceu?'))
idade = 2022-nasc
if idade<=9:
    print('Sua categoria é MIRIM.')
elif 9<idade<=14:
    print('Sua categoria é INFANTIL.')
elif 14<idade<=19:
    print('Sua categoria é JUNIOR.')
elif idade==20:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
