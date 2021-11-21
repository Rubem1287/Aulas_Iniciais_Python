
usuario = input('nome do usuário :')
senha = int(input('digite a senha do usuário :'))

usuario_bd = 'rubem'
senha_bd = 123

if usuario_bd == usuario and senha == senha_bd:
    print('Login feito com sucesso')

else:
    print('Usuario ou senha incorretos')

print()
a = 2
b = 3

if not b > a:  # Negação mesmo o valor de B sendo maior
    print('B é maior que A')

else:
    print('A é maior B')


a = ''
b = 3

if not a:  # como se tivesse falando se A é null então executa o código
    print('Por favor preencha o valor de A')

a = 2
b = 0

if not b:  # como se tivesse falando se A é null então executa o código
    print('Por favor preencha o valor de B')

nome = 'rubem'

if 'u' in nome:  # Comparando
    print('Existe a Letra u no seu nome')

if 'bem' in nome:  # Comparando
    print('Existe bem no seu nome')

if 'x' in nome:  # Comparando
    print('Existe x no seu nome')
else:
    print('Não existe x no seu nome')

if 'x' not in nome:  # Comparando
    print('Executou o código')
else:
    print('Não executou o codigo')
