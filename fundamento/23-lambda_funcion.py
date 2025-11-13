# 1 - Função de potencia de um número
power = lambda num: num ** 2
print(power(8))
print(power(9))

# Verificar se um numero é par
is_even = lambda x: x % 2 == 0
print(is_even(25))
print(is_even(30))

# 3 - Funçãp que divide um numero por outro
div_num = lambda x, y: x / y
print(div_num(600, 30))

# 4 - Função que inverte uma string
reverse_string = lambda s:  s [::-1]
print(reverse_string("Python"))

# 5 - Funcionalidades realacionadas aos filmes
movie_list = ["Invocação do mal", "Halloween", "O chamado", "A bruxa"]
ratings = {
    "Invocação do mal": [9.9, 6.9, 8.8],
    "Halloween": [10, 9.6, 8.9],
    "O chamado": [7.7, 8.5, 6.6],
    "A bruxa": [6.6, 5.5, 3.0]
}
# Função para calcular a média das avaliações
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

# Função para verificar se um filme está na lista
check_list = lambda movie_name: movie_name in movie_list

# Função para recomendar um filme com base na avaliação média
recommend_movie = lambda movie_name: f"Recomendo assistir o {movie_name} com média de {average_rating(movie_name):.2f}"

print(f"Média de avaliação de Halloween é: {average_rating("Halloween")}")
print(f"O chamado está na lista? {check_list("O chamado")}")
print(recommend_movie("A bruxa"))