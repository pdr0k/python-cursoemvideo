#Aninhar - colocar uma coisa dentro da outra

#3 caminhos
#se for para direita:

#se não se:

#se:


#ou seja,

#if carro.esquerda():
  #  bloco 1
#elif carro.direita():
  #  bloco 2
#else:
  #  bloco 3

#A primeira condição vai ser sempre 'if'
#a segunda até a penúltima sempre e'lif'
# e a última 'else'
#if e else somente uma vez começo e fim, elif quantas quiser
# else é opcional, se retirar , não faz diferença

nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Nome bosta')
print(f'Tenha um bom dia, {nome}.')


