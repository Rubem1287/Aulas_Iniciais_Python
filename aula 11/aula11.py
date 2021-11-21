nome = input('Qual o seu nome ? ')
idade = int(input('Qual a sua idade ? '))

if idade >= 20 and idade <= 30:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} não pode pegar o empréstimo')

num1 = 2
num2 = 2
print()
expressao = (num1 == num2)

print(expressao)  # Verdadeiro

num1 = 2
num2 = 2
print()
expressao = (num1 > num2)

print(expressao)  # Falso

num1 = 2
num2 = 2
print()
expressao = (num1 >= num2)

print(expressao)  # Verdadeiro

num1 = 2
num2 = 2
print()
expressao = (num1 < num2)

print(expressao)  # Falso

num1 = 2
num2 = 2
print()
expressao = (num1 <= num2)  # Verdadeiro

print(expressao)

num1 = 2
num2 = 2
print()
expressao = (num1 != num2)  # (!=Diferente) False

print(expressao)
