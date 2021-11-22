
print()

usuario = input('Digite seu usuário :')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa ter mais que 6 caracteres para ser cadastrado.')

else:
    print('Você foi cadastrado no sistema.')


string1 = input('digite algo :')
string2 = input('digite algo :')

print(f'A quantidade de total de caracteres digitados foi {len(string1)+len(string2)}')

