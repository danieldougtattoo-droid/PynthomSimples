"""
* args - Utilizamos ela quando não temos certeza de quantos argumentos 
usamos em uma funçao.
- Os argumentos são usados como uma tupla.
** kwargs - Além dos valores podemos passar também as 
respectivas chaves para cada argumento.
Os argumentos são passados como um dicionário.
"""
# - 1 soma de números
from unicodedata import category


def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"A soma é: {sum_total}")

sum(7,7)
sum(7,9,10,20)
sum(100,800)

# 2 - Apresentação de curso
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de cursos:")
presentation(name="Python", category="backend", level="Iniciante")
presentation(name="Visão computacional com python", category="IA", level="Avançado")
presentation(name="DashBoards com dash", category="Data Science", level="Intermediario")

