#Vamos fazer uma simples calculadora...

while True:

    def calc(num1, operador, num2):
        if operador == "+":
            return num1 + num2
        elif operador == "-":
            return num1 - num2
        elif operador == "x":
            return num1 * num2
        elif operador == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Nada é divisível por Zero."
            
    
    num1 = float(input("Digite um número: "))
    operador = input("Digite um operador: ")
    num2 = float(input("Digite um número: "))

    resultado = calc(num1, operador, num2)

    print(f"Resultado: {resultado}")

