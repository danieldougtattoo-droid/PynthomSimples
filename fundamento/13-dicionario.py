filmInception = {
     "title": "Inception",
     "yearRealised": 2010,
     "imdbRating": 8.8,
     "genres": ["Action", "Adventure", "Sci-fi"]
}
print(filmInception)
print(len(filmInception))
print(type(filmInception))

# 1 - RECUPERAR ELEMENTOS DO DICIONÁRIO
print(filmInception["genres"])
print(filmInception.get("imdbRating"))

# 2 - BUSCAR APENAS AS CHAVES DO DICIONÁRIO
print(filmInception.keys())

# 3 - BUSCAR APENAS OS VALORES DO DICIONÁRIO
print(filmInception.values())

# 4 - BUSCAR ITENS COM CHAVES E VALORES
print(filmInception.items())

# 5 - ADICIONAR NOVO ITEM AO DICIONÁRIO
filmInception["Diretor"] = "Chistopher Nolan"
print(filmInception)

# 6 - ATUALIZAR ITENS NO DICIONÁRO
filmInception.update({"imdbRating": 9.0})
print(filmInception)

# 7 - REMOVER ITENS DO DICIONÁRIO
filmInception.pop("Diretor")
print(filmInception)