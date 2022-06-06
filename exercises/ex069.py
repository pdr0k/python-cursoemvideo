#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostra:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

count_18 = count_man = count_woman20 = 0
while True:
    print('-'*30, 'CADASTRE UMA PESSOA', '-'*30)
    age = int(input('Idade: '))
    if age > 18:
        count_18 += 1

    gender = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while gender not in 'MF':
        gender = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if gender == 'M':
        count_man += 1

    if gender == 'F' and age < 20:
        count_woman20 += 1

    choice = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while choice not in 'SN':
        choice = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if choice == 'S':
        continue
    else:
        print('-'*30)
        break


print(f'{count_18} pessoas têm mais de 18 anos.')
print(f'{count_man} homens foram cadastrados.')
print(f'{count_woman20} mulheres possuem menos de 20 anos.')







