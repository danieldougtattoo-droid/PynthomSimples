name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digitte o ano de lançamento:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print("Dados do filme:")
print("=====================")
# Alternativa 1
#  print("Nome do filme:",name)
#  print("Ano de lançamento:",yearLaunch)
#  print("Nota do filme:",noteMovie)

# Alternativa 2
# print("Nome do Filme:", name, "\nAno de Lançamento:", yearLaunch, "\nNota do Filme:", noteMovie)

# Alternativa 3
print(f"Nome do filme: {name}\n"
      f"Ano de Lançamento: {yearLaunch}\n"
      f"Nota do Filme: {noteMovie}\n"
       )