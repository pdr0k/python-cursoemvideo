#035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#042 - Refazer, acrescentando  orecurso de mostrar que tipo de triângulo será formado.
#- Equilátero, todos os lados iguais.
#- Isósceles, dois lados iguais.
#- Escaleno: todos os lados diferentes.

a = float(input('Dê um comprimento de reta: '))
b = float(input('Dê outro comprimento de reta: '))
c = float(input('Dê o último comprimento de reta: '))

if a+b>c and b+c>a and a+c>b:
    print('Pode formar um triângulo.')
    if a==b==c:
        print('O triângulo formado será equilátero.')
    elif a==b or b==c or c==a:
        print('O triângulo formado será isósceles.')
    else:
        print('O triângulo formado será escaleno.')
else:
    print('Não pode formar um triângulo.')
