# 1 - Função para imprimir uma mensagem
def Welcome():
    print("Bem-vindo ao Sistema de filmes!")

# for i in range(10):
#  Welcome()

# 2 - Funçao para calcular a média de notas
def calculate_average():
    num_ratings = int(input("Digite o numero de avaliações:\n"))
    total = 0 
    for i in range(num_ratings):
        note = float(input(f"Digite a nota {i+1}:\n"))
        total += note

    if num_ratings > 0: 
            average = total / num_ratings
    else:
            average = 0

    return average

print(f"A média de notas é: {calculate_average():.2f}")

# 3 - Função para cadastrar um filme
def create_movie():
    nome = input("Digite o nome do filme:\n")
    yearLaunch = int(input("Digitte o ano de lançamento:\n"))
    moviePrice = float(input("Digete o preço do filme:\n"))
    ratting = float(input("Digite a nota do filme:\n"))
    print(f"{nome} ({yearLaunch}) - R$ {moviePrice:.2f}")

create_movie()


