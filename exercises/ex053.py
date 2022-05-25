#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.



txt = str(input('Digite um texto:')).upper().strip().replace(' ','')
if txt == txt[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

outra forma

#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range(len(junto) -1, -1, -1):
    #inverso += junto[letra]
#if inverso == junto:
    #print('Temos um palíndromo!')
#else:
    #print('A frase digitada não é um palíndromo!')