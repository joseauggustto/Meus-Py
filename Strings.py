name = 'José'
age = 22 
score = 80.9
altura = 1.89

# Comando isinstance e type. 
 
print(name ,type(name))
print(age, type(age))
print(score, isinstance(score, float))
print(altura, isinstance(altura, float))

#Aspas duplas para a String, informando que é uma citação.

print('She said, "Hello"')
my_str = "Hello"

#Comando in, usado para saber se existe aquilo na string

print("Hello" in my_str)
print('World' in my_str)

#Comando len, usado para saber quantos caracteres tem a String

print(len(my_str))

#Para selecionar um caractere pelo número, basta por [] com o número dentro.

alo = 'olameunoméaí'
print(alo[5])
print(alo[1:6]) #lembre-se que ele conta a partir do 0, a saída aqui será 'lameu'
print(alo[2:7:2])
print(alo[::-1])

#Concatenando Strings
my_string_1 = 'oi'
my_string_2 = 'olá'

exit = my_string_1 + ' ' + my_string_2
print(exit)

# Todos os carcateres de uma string em maíusculo

aloupper = alo.upper()
print(aloupper)