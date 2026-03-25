# Vamos lá...
# Estudo sobra laços e seqûencias.

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


