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

# Todos os carcateres de uma string em maíusculo ou minúsculo 

aloupper = alo.upper()
print(aloupper) 

alolower = alo.lower()
print(alolower)

# Para remover os espaços em branco é só usar Strip

alostripr = alo.strip()
print(alostripr)

#Para substituir uma palavra por outra, usa o comando replace(old, new)

#Para separar as palavras de uma String é só usar o comando Split

#O comando Join desfaz o que o Split faz

#-------------------------------------------------

#Construindo um gerador de perfil

first_name = 'John'
last_name = "Doe"
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28

employee_info = full_name + ' is ' + str(employee_age) + ' years old.'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

position = 'Data Analyst'
salary = str(75000)
employee_card = (f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}')
print(employee_card)

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
print(year_code)

initials = employee_code[9:11]
print(initials)

last_three = employee_code[-3:]
print(last_three)