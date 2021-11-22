print()
num1 = input('digite um número :')
num2 = input('digite um número :')

if num1.isdigit() and num2.isdigit():
    num1=int(num1)
    num2=int(num2)
    
    print(num1+num2)
    
else:
    print('Não pude converter os números em inteiro para fazer contas.')