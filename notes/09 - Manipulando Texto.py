#String = cadeia de caracteres

#frase = 'Curso em Vídeo Python'

#FATIAMENTO DE STRING:
#frase[9] - pega o nono caractere da string
#frase[9:13] - pega do 9 até o 12
#frase[9:21:2] - pega do 9 até o 20 pulando de 2 em 2
#frase[:5] - começa do 0 e vai ate o 4
#frase[15:] - começa do 15 até o 20
#frase[9::3] - começa no 9 até o final pulando de 3 em 3

#ANÁLISE

# len(frase) - length (comprimento da frase)
# frase.count('o') - conta quantas vezes a letra 'o' aparece
        # frase.count('o', 0, 13) - quantos 'o's existem do 0 ao 12
# frase.find('deo') - encontra a posição de onde se inicia o 'deo'
        # frase.find('Android') - retorna o valor -1, já que Android não existe na frase
# 'Curso' in frase - existe curso in frase? Retorna True or False

#TRANSFORMAÇÃO

#frase.replace('Python','Android') - substitui python por android secundariamente
#frase.upper() - o que já for maiusculo mantém, o que não for troca
#frase.lower() - o que já for minusculo mantém, o que não for troca
#frase.capitalize() - Coloca todos os caracteres em minusculo, e deixa só a primeira letra da string maiuscula
#frase.title() - analisa quantas palavras têm e transforma as primeiras letras em maiúscula

#ATENÇÃO FRASE 2
#frase2 = ---Aprenda Python-- / (- é espaço)

#frase2.strip() - remove todos os espaços no início e final da string
#frase2.rstrip() - remove todos os espaços no final
#frase2.lstrip() - remove todos os espaços do início

#DIVISÃO

#frase.split() - cria uma lista com todas as palavras de uma string, separando tudo e renumerando
#PYTHON É LEGAL
#012345678910111213
# vai ficar: PYTHON É LEGAL
#            012345 0 01234
#              1    2   3

#JUNÇÃO

#'-'.join(frase) - junta os 4 elementos da frase e separa com o '-'


frase = 'Curso em Vídeo Python'
#print(frase.upper().count('O'))
#print(len(frase.strip())
print(frase.replace('Python','Android'))

#strings são imutáveis, a não ser que eu use uma função de transformação e depois atribua isso a uma variável

#print("""ASUIDHJHUASDHUASDHUASDHUASHDUHUASD
#ASDHUHASUDHUASDHUASDHUASHDUHUASDHU
#AHUSHUASDHUASDHUASDHUASD
#AHUSHUASDHUASDHUASD""")
#3x aspas duplas coloca um texto inteiro q ta em diferentes linhas

#dividindo a frase em lista fica:

#frase = 'Curso em Vídeo Python'
#dividido = frase.split()
#print(dividido[0])

#print(dividido[2][3]) - mostra a letra 3 da palavra 2