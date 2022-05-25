#Laços de Repetição
#ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE


#exemplo do personagem com os blocos e passos para pegar a maçâ
#laço c no intervalo(1,10)
#    passo
#pega


#for c in range(1,10):
#   passo
#pega


#colocando mais de dois comandos, como passo e pula:  !!!!ATENÇÃO À ITERAÇÃO!!!
#for c in range(1,3):
#   passo
#   pula
#passo
#pega


#com condição dentro, como pegar uma moeda:
#for c in range(0,3):
#if ter moeda:
#       pega
#   passo
#   pula
#passo
#pega


for c in range(0, 6):
    print(c)
#ele vai contar do 0 até o 5, desconsiderando o último número
for c in range(1,6):
    print(c)
#vai contar de 1 até 5


for c in range(6,0, -1): (contando para trás)
    print(c)


for c in range (0,7,2): (contando de dois em dois)
    print(c)

n = int(input('Digite um número:')) #vai contar até o n, por isso n+1, já que o python desconsidera o último
for c in range (0,n+1):
    print(c)


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)


for c in range(0, 3): #vai ler e repetir 3x
    n = int(input('Digite um valor '))
print('fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}. ')
 