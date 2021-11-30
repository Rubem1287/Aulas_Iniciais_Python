#Sempre que quiser pegar o último caracter de ums string usar o indice -1

#Indices + [012345678] positivos
texto    = 'Python_S2'
#Indices - [987654321] negativos

print(texto[2]) # acessando partes da string com números positivos

print(texto[-2])  # acessando partes da string com números negativos

novastring = texto[2:6]
#novastring = texto[:6]

print(novastring) # fatiando strings com indice positivo

novastring1 = texto[-9:-1]
#novastring = texto[:-1] ele pega do inicio e vai áte o indice menos -1

print(novastring1)  # fatiando strings

novastring2 = texto[1:6:2]# aqui vou estar pulando de 2 em 2


print(novastring2)  # fatiando strings com indice positivo
