# # Lista de filmes
# movieslist = ["O exorcista" , "Invocação do Mal", "Anna Bele", "Padre"]

# # 1 - Interando valores de uma lista
# for movie in movieslist:
#     print(movie)

# # 2 - Quando a condição for atendida, o loop é encerrado

#     for movie in movieslist:
#         if movie == "Anna Bele":
#             break
#         print(movie)

# # 3 - Quando a condição for atendida, o loop vai para próxima interação
# for movie in movieslist:
#     if movie == "Invocação do Mal":
#         continue
#     print(movie)

# 4 - Avaliação do filme
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0.0

for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note 

if movieRating > 0:
    average = total / movieRating 
else:
    average = 0.0

print(f"Média de avaliação do filme: {movieName} é: {average:.2f}")
lista = [1,2,3]
lista.append(4) 
print(lista)

