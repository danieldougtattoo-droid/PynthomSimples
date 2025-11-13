import random

# 1- Selecione valor aleatório de uma lista
list1 = [4, 5, 9, 15, 3, 11]
print(random.choice(list1))

# 2- Gera um número aleatória em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# 3- Seleciona caractere aleiatório de uma string
name = "Python é legal"
r2 = random.choice(name)
print(r2)

# 4- Selecione mais de um valor aleiatório
#random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "Ola mundo"
print(random.sample(s, 2))
