expressao_matematica = input("Digite uma expressão matemática: ")

if "/" in expressao_matematica and '0' in expressao_matematica.split("/"):
    print("Desculpe, mas é impossível dividir por 0.")
else:
    resultado = eval(expressao_matematica)
    print("O resultado é", resultado)











