"""
Tipos de dados

str - string(Textos ('texto' "texto"))
int - inteiro(Números inteiros(0, 10, 20, 30 etc...), números positivos ou negativos que não tenha pontos)
float - real/ponto flutuante(Números(10.20, 20.10, 30.50 etc...) números positivos ou negativos com pontos)
bool - booleano/lógico(true/false(verdadeiro ou falso),(10==10 (10 é igual a 10?) == verdadeiro))

"""

print('Luiz', type('Luiz'))
print(10, type(10))
print(25.23, type(25.23))
print(10==10, type(10==10))
print(11==10, type(11==10))
print(bool(0))#coisas vazias são false
print('Luiz', type('Luiz'), bool('luiz'))
print('10', type('10'), type(int('10')))

print('##Exercício##\n')
#string : Nome
print('Rubem', type('Rubem'), '\n')

#int : Idade
print(34, type(34), '\n')

#float : Altura
print(1.70, type(1.70), '\n')

#bool : Boleano/Lógico (Verificar se minha idade é maior que 18 anos)
print(34>=18, type(34>=18))
