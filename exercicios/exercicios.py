
#Primeiro exercício
print()

numeros = input('Digite um número inteiro :')
if numeros.isdigit():
    numero = int(numeros)

    if numero == 0:
        print('0 é neutro.')
        
    elif numero % 2 == 0:
        print('Esse número é Par.')
    
    else:
        print('Esse número é Impar.')
        
else:
    print('Isso que foi digitado não é um número inteiro.')
    
    
    
    #Segundo exercicio
horario = input('Digite a hora entre 0 a 23 :')

if horario.isdigit():
    hora = int(horario)
    if hora >= 0 and hora <= 23:
        if hora >= 0 and hora <= 11:
            print('Bom dia.')
    
        elif hora >= 12 and hora <= 17:
            print('Boa tarde.')
    
        elif hora >= 18 and hora <= 23:
            print('Boa noite.')
        
    else:
        print('Erro: O horário aceito é entre 0 a 23 horas.')
        
else:
    print('O que foi digitado não é um hora.')
     
    
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
