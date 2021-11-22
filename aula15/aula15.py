
print()
num1 = 1
print(f'{num1:0>10}')#Vai mostrar 9 zeros a esquerda e depois o 1 exemplo:0000000001, ou seja 10 casas contando como 1

num2 = 1150
print(f'{num2:0>10}') #vai mostrar 6 zeros a esquerda e depois o 1150 exe: 0000001150, ou seja ao todo 10 casas contando com o 1150

num2 = 1151
print(f'{num2:0<10}')#vai mostrar 6 zeros a direita e depois o 1151 exe: 1151000000, ou seja ao todo 10 casas contando com o 1151

num2 = 1151
print(f'{num2:0^10}')#vai dividir 6 zeros a direita e a esquerda e centralizar nosso número exe: 0001151000

num2 = 1150
print(f'{num2:0>10.2f}')#vai mostrar 3 zeros a esquerda e colocar o 1150 e depois .00 exe: 0001150.00, o ponto tmb conta como caracter

nome = 'Rubem Eduardo'
nome_formatado = '{:@>13}'.format(nome)
print(nome_formatado) #Não vai adicionar nada, por que meu nome já tem 12 caracter

nome = 'Rubem Eduardo'
nome_formatado = '{:@>15}'.format(nome)
print(nome_formatado) #Agora meu nome vai ficar com 2 @ a direita dele exe: @@Rubem Eduardo, não esqueca que o espaço conta como caracter

nome = 'Rubem'
sobre_nome = 'Eduardo'
nome_formatado = '{0:@^30} {1:#^20}'.format(nome, sobre_nome)
print(nome_formatado)  # Irá acessar o sobre nome, por que ele é a posição 1 e nome que é posição 0 e irá mostar exe: @@@@@@@@@@@@Rubem@@@@@@@@@@@@@ ######Eduardo#######

nome = 'Rubem Eduardo'
print(nome.upper()) #Todas as letras maiúsculas
print(nome.lower())  # Todas as letras minúscula
print(nome.title())  # Primeiras letras maiúsculas
