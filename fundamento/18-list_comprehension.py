# 1 - listando valores de 0 a 10 que sejam menores que 5
for i in range(10):
    if i < 4:
        print(i)
# 2 - Agora pelo list comprehension
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# 3 - Filmes que possuem a letra "e" no titulo

movieslist = ["O exorcista" , "Invocação do Mal", "Anna Bele", "Padre"]
moviesWithE = [movie for movie in movieslist if 'e' in movie.lower()]
print(moviesWithE)

# 4 - Filmes que eu assisti
moviesWacthed = [movie for movie in movieslist if movie != "O exorcista"]
print(moviesWacthed)

# 5 - Encontrando um filme pelo nome
while True: 
    searchName = input("Digite o nome do filme para buscar na lista(ou sair para encerrar):\n")
    if searchName.lower() == 'sair':
     print("Programa Encerrado")
    break

foundMovies = [movie for movie in movieslist if searchName.lower() in movie.lower()]
if foundMovies:
    print(f"fimle(s) encontrado(s) com o nome: {searchName}:")
    for foundMovie in foundMovies:
        print(foundMovies)
    else:
        print(f"Nenhum filme encontrado com o nome: {searchName}. Tente novamente.")
