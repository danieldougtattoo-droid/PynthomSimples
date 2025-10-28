# # INFORMAÇÕES SOBRE O FILME
# nome = input("Digite o nome do filme:/n ")
# yearRelease = int(input("Digite o ano de lançamento do filme:/n "))
# rating = float(input("Digite a avaliação do filme:/n"))

# # VERIFICAR  SE O FILME É RECOMENDADO
# if rating > 8.0 and yearRelease > 2015:
#     print(f"O filme {nome} é recomendado!")
# else:
#     print(f"O filme {nome} não é recomendado.")

#     print(type(nome))

num1 = float(input("Digite o primeiro número:/n"))
num2 = float(input("Digite o segundo número:/n"))
operation = input("Digite a operação: (+ - * /)/n").strip()

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2 

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por Zero.")
        result = 0
else:
    print("Operação inválida")
    result = 0

print(f"O resultado da operação é: {result:.2f}")
