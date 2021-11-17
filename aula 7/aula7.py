# Nomes de variaveis ou objetos : Iniciar com letra, pode conter números, separar_, letras minúsculas

nome = 'Rubem'
idade = 33
altura = 1.80
e_maior = idade >= 18
peso = 80
imc = (80/(1.80**2))

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print(nome, 'tem', idade, 'anos de idade e seu imc é :', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é : {imc:.2f}')
print('{0} tem {1} anos de idade e seu imc é : {2}'.format(
    nome, idade, imc))  # Referente 0 = nome, 1 = idade, 2=imc
print('{n} tem {i} anos de idade e seu imc é : {im}'.format(
    n=nome, i=idade, im=imc))
