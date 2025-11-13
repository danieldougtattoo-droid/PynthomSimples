# Lista de filmes
movieslist = ["O exorcista" , "Invocação do Mal", "Anna Bele", "Padre"]
print(len(movieslist))

# 1 - Interando valores de uma lista usando while
index = 0
while index < len(movieslist): 
    print(movieslist[index])
    index += 1

# 2 - Quando a condição for atendida, o loop é encerrado
index = 0
while index < len(movieslist):
    if movieslist[index] == "Anna Bele":
        break
    print(movieslist[index])
    index += 1

# 3 - Quando a condição for atendida, o loop vai para a próxima interação
index = 0
while index < len(movieslist):
    if movieslist[index] == "Invocação do mal":
        continue
    print(movieslist[index])
    index += 1

# 4 - Avaliação do filme usando while
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))
total = 0
count = 0
while count < movieRating:
 note = float(input("Digite a nota para o filme:\n"))
 total = note
 count += 1
if movieRating > 0:
    avarage = total / movieRating
else:
        avarage = 0.0 


print(f"Média de avaliação do filme: {movieName} é: {avarage:.2f}")

