#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
gender = ''
while gender != 'M' and gender != 'F':
    gender = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()
    if gender != 'M' and gender != 'F':
        print('Tente Novamente.')
print('Entendi.')


pode ser feito da seguinte forma também
sexo = str(input('Digite seu sexo')).strip().upper()[0] #só a primeira letra do upper
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')