#Melhore o Desafio 061, pergutando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA :'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end ='')
        termo += razao
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print(f'Progressão finalizada com {total} termos mostrados.')