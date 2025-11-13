# 1 - Função para imprimir um nome completo
def full_name(first_name, last_name):
    print(f"Nome é: {first_name} {last_name}")

full_name("Daniel", "Carvalho")

# 2 - Função para somar dois numeros
def sum_numbrs(a, b):
    return a + b

print(f"A soma é: {sum_numbrs(10, 90)}")

# 3 - Função com parâmetro default
def addrees(country):
    print(f"Eu moro em: {country}")

addrees("Noruega")

# 4 - Função para avaliar um filme
def rate_movie(numb_rating, name_movie):
    total = 0
    for i in range(numb_rating):
        note = float(input("Digite a nota do filme:\n"))
        total += note

    if numb_rating > 0:
        average = total / numb_rating
    else: 
        average = 0

    print(f"A média de avaliação do filme {name_movie} é: {average:.2f}")

rate_movie(3, "Halloween")
    