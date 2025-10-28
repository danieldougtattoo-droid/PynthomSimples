movieName = "Top Gun"
movieDescription = """
 Top Gun: Maverick é um filme
            de ação e aventura
          muito consagrado
            pela indústria
          """
print(movieName.upper()) # Todas Letras maiúsculas
print(movieName.lower()) # Todas Letras minúsculas
print(movieName.title()) # Primeiras Letras maiúsculas de cada palavra
print(movieName.capitalize()) # Primeira letra maiúscula
print(movieName.center(10, "-")) # Retorna string centralizada caracter de preenchimento
print(movieName.find("n")) # Retorna o índice da primeira ocorrência do caractere
print(movieName.find("o")) # Retorna a posição de um determinado caractere
print(movieName.replace("top", "maverick")) # Substitue uma palavra por outra
print(movieName.split(',')) # Divide a string em uma lista de palavras