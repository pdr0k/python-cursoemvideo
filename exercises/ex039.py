#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é hora de se alistamento.
#- Se já passou do tempo do alistamento
#Seu programa também deverá mostraro tempo que falta ou que passou do prazo.


ano = int(input('Que ano você nasceu?'))
idade = 2022-ano
anos_alistamento = 18-idade
if idade>18:
    print('Seu alistamento está atrasado.')
elif idade==18:
    print('Está na hora de se alistar.')
elif idade<18 and anos_alistamento>1:
    print(f'Ainda faltam {anos_alistamento} anos para você se alistar.')
else:
    print(f'Ainda falta {anos_alistamento} ano para você se alistar.')