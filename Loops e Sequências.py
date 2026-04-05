# Vamos lá...
"""Estudo sobra laços e seqûencias.

countries = ['Brazil', 'Australia', 'Suíça']
print(countries[2])

countries = ['Brazil', 'Australia', 'Suíça']
print(countries[-1])

nome = "Augusto"
print(list(nome))

sei_la = [3, 4, 6, 3, 2 , 65, 6 , 67]
print(len(sei_la))

languages = ["espanhol", "english"]
languages[0] = "pt br"   # att valor, AAAAAAAA
print(languages)

languages = ["espanhol", "english"]
del languages[0]   # deletar valor da lista
print(languages)

programming_languages = ['Python', 'Java', 'C++', 'Rust']    # saber se algo está ali...
print("Rust" in programming_languages)
print("JavaScripty" in programming_languages)

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2]) # vai dar a segunda lista de dentro

developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer
print(name)
print(rest)

"""

print("-" * 30)

"""
.append adiciona um novo elemento a lista, criando uma sub lista inside ()

.extend faz com que adicione outros elementos na lista, sem criar sublista []

.insert adiciona um valor específico em um local específico na lista. Coloca onde eu quero o vizinho e depois o valor que eu quero como vizinho à direita. ()

.remove vai remover um dado específico da lista, coloca o número entre ()

.pop vai remover um elemento específico de acordo com o índice determinado, se eu colocar () vazio vai remover o último dado.

.clear já tá dizendo, vai foder com tudo

.sort vai reorganizar a lista do < para >, .sorted vai refazer uma lista nova, só que organizada. 

.reverse vai coloca a lista de trás para frente.

o comando .index serve para procurar na lista um valor específico retornando sua posição. 

"""
print("-" * 30)

# numberss = [1, 2, 3, 4, 5]
# numberss.append(6)
# print(numberss)

# numbers = [1, 2, 3, 4, 5]
# outersnbrs = [6, 7, 8]
# numbers.append(outersnbrs)
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# outersnbrs = [6, 7, 8]
# numbers.extend(outersnbrs)
# print(numbers)

# alo = [1, 2, 3, 4, 5]
# alo.insert(3, 2.5)  #adicionar em um local específico...
# print(alo)

print("-" * 30)

"""
Tuplas em python são dados semelhantes a listas, a diferença é que listas são mutáveis e tuplas não. Listas são assim: [] e tuplas são assim ().

Para acessar um elemento da tupla, use [].

Para saber se algum dado está em uma tupla usa-se o in.

O argumento sorted() + key=len organiza os elementos da tupla por comprimento.

"""
print("-" * 30)

"""
LOOPS

Os loops é uma forma de repetir argumentos em python. 

Para repetir uma lista no console, usamos o "for". ex: (for language in programming_languages)

O comando char vai traçar letra por letra de uma string em um print. 

temos o comando break e continue, são irmãos com propostas diferentes. O break para quando achar o item desejado e o exclui, o continue continua excluindo o item desejado.

####

# programming_languages = ['Rust', 'Java', 'Python', 'C++']

# for languages in programming_languages:
#     print(languages)


# for char in 'Augusto':
#     print(char)


# categorias = ['Fruit', 'Vegetable']
# foods = ['Apple', 'Carrot', 'Banana']

# for category in categorias:
#     for food in foods:
#         print(category, food)

"""

print("-" * 30)

# Jogo de advinhação 

# correct_number = 3

# while True:
#     advinhar = int(input("Advinhe o número entre 1 e 10: "))

#     if advinhar == correct_number:
#         print("Você conseguiu!")
#         break         #Descobri esse comando novo, muito bom! 
#     else:
#         print("Errou, tente novamente!")

# palavras = ['sky', 'apple', 'rhythm', 'fly', 'orange']

# for palavra in palavras:      # esse comando faz com que cada palavra da lista "palavras" seja armazenada temporariamente na váriavel 'palavra'. 
#     for letras in palavra:     # esse comando é interno, ele vai rodar letra por letra da palavra armazenada temporariamente.
#         if letras.lower() in "aeiou":    # o comando lower() tranforma tudo em minúscula pra não gerar erros e o "if in" vai ver se tem vogais dentro das palavras.
#             print(f"'{palavra}' contem a vogal '{letras}'")
#             break              # se ele achou uma vogal nas palavras, ele para e imprime, não vai ficar lendo mais o resto da palavra.
#     else:                          # cometi um pequeno erro de indentação aqui, se o else estiver ligado ao if, ele vai imprimir uma condição para cada letra, e não só pra palavra
#         print(f"'{palavra}' não tem vogal")


"""
RANGE

o range é usado para criar uma sequencia de numeros inteiros.
Sintaxe básica da função range: range(start, stop, step)
O argumento stop é obrigatório, o start não tanto porque ele vai iniciar com 0 por padrão.

"""
# for num in range(4): # aqui ele vai gerar uma sequencia até chegar no 3, começando do 0.
#     print(num)

# for num in range(2, 6):
#     print(num)

# for num in range(2, 11, 2):
#     print(num)

# number = list(range(10))  #vai criar uma lista de número no range especificado.
# print(number)

print("-" * 30)

"""
Enumerate e Zip

Para enumerar uma lista com seu respectivo numero, usamos a função enumerate.

O comando zip é usado para unir duas listas com seus enumerates.

"""

# languages = ['Spanish', 'English', 'Russian', 'Chinese']
# for index, language in enumerate(languages, 1):  #ou posso usar start=1 
#     print(f'Num {index} language: {language}')

# #--------------

# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]

# for name, id in zip(developers, ids):
#     print(f"Name: {name}")
#     print(f"ID: {id}")


print("-" * 30)

"""
List Comprehensions 

esse comando é usado para deixar o código menor e mais fácil de leitura. 

a função filter é usada para filtrar em uma lista os dados de acordo com uma condicao espécifica

a função map faz com que funções seja executadas em listas

"""

"""pares = []

for num in range(21):
    if num % 2 == 0:
        pares.append(num)

print(pares)

# list comprehensions

pares = [num for num in range(21) if num %2 == 0]
print(pares)

#---------------------

# numeros = range(16)
# resultado = [(num, "Par") if num %2 == 0 else (num, "Impar") for num in numeros]
# print(resultado)

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
def palavra_longa(words):
    return len(words) > 4
palavra_longa = list(filter(palavra_longa, words))
print(palavra_longa)

longwords = list(filter(lambda w: len(w) > 4, words))
print(longwords)

#------------------

num = [2, 4, 6, 9]

def mult(num):
    return (num * 2)

result = list(map(mult, num))
print(result)

# ----------------------

multi = list(map(lambda x: x * 2, num))
print(multi)
"""
print("-" * 30)

"""
Lambda Functions 

A função lambda serve para criar uma função descartável e rápida. Mas pode ser chamada de anonima.
Essa função pode ser útil em casos especiais que é necessário fazer uma lógica rápida, mas em casos mais complexos é melhor criar uma função def.
Os melhores casos para se usar é quando vai ser necessário mexer com filter e map.

"""

