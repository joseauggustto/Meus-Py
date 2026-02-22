n = input("Digita essa porra aqui: ")

print("Qual o tipo primitivo desse valor? ", type(n))
print("Tem espaços? ", n.isspace())
print("É um número? ", n.isnumeric())
print("É alpha? ", n.isalpha())
print("É alphanumérico? ", n.isalnum())
print("Está em maiúsculas? ", n.isupper())
print("Está em minúsculas? ", n.islower())
print("Está capitalizada? ", n.istitle())

