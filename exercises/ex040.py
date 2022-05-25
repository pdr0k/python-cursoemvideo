#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0 -> Reprovado
#- Média entre 5.0 e 6.9 -> RECUPERAÇÃO
#- Média 7.0 ou superior -> Aprovado


n1 = float(input('Qual foi sua primeira nota?'))
n2 = float(input('Qual foi a sua segunda nota?'))
media = (n1+n2)/2
if media <5.0:
    print(f'Sua média foi: {media:.1f}, portanto, você está reprovado.')
elif 5.0<=media<=6.9:
    print(f'Sua média foi: {media:.1f}, portanto, você está de recuperação.')
else:
    print(f'Sua média foi: {media:.1f}, portanto, você está aprovado.')
