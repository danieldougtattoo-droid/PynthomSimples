num1 = int(input("Digite o primeiro numero: \n"))
num2 = int(input("Digite o segundo numero: \n"))

# Aritmeticos
sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2

print(f"Potência do número {num1} por {num2} é: {exp}") 
print(f"Resto da divisão do número {num1} por {num2} é: {mod}")

# Comparações
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
differnt = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"OS números são iguais? {equal}")
print(f"O número {num1} é maior que o número {num2}? {bigger}")

# Atribuição
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1  -1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1