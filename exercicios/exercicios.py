
#Primeiro exercício
print()

numero = int(input('digite um número inteiro :'))

if numero % 2 == 0:
    print('Esse número é inteiro.')
    
else:
    print('Esse número não é inteiro.')
    
    
    #Segundo exercicio
hora = int(input('digite a hora :'))

if hora >= 0 and hora <= 11:
    print('Bom dia.')
    
elif hora >= 12 and hora <= 17:
    print('Boa tarde.')
    
elif hora >= 18 and hora <= 23:
    print('Boa noite.')
    
    
    #Terceiro exercicio
print()    
primeiro_nome = input('Digite o primeiro nome :')

quantidade_letras = len(primeiro_nome)
    
if quantidade_letras >= 0 and quantidade_letras <= 4:
    print('Seu nome é curto.')
    print()
elif quantidade_letras >= 5 and quantidade_letras <= 6:
    print('Seu nome é normal.')
    print()
elif quantidade_letras > 6:
    print('Seu nome é muito grande.')
    print()
