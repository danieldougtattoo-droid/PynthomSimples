movieName = "Top Gun"
# string[ínicio:fim] - Índice começao na posição 0 | índice final - 1

# 1 - Buscar toda string através da posição
print(movieName[0:])

# Buscar toda string até a ultima posição
print(movieName[:7])

# Buscar toda string da terceira até a última posiçao
print(movieName[2:])

"""
String[início:Fim:Passo]
índice começa na posiçao 0 | índice final - 1 
passo - determina o incremento. Por padrão esse numero é o 1.
"""
# 2 - Buscar toda string de 2 em 2 posições
print(movieName[::2])

# 3 - Buscar toda string no índice impar
print(movieName[1::2])

# 4 - Inverter uma string de trás para frente
print(movieName[::-1])