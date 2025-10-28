import pprint

filmsDict = {
    "Inception": {
        "yearRealised": 2010,
        "imdbRating": 8.8,
        "genres": ["Action", "Adventure", "thriller"]
    },
    "Interstellar": {
         "yearRealised": 2014,
        "imdbRating": 8.6,
        "genres": ["sci-fi","drama"]
    },
    "The Dark Knight": {
        "yearRealised": 2008,
        "imdbRating": 9.0,
        "genres": ["action", "crime", "drama"]
    }

}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - BUSCAR INFORMAÇÕES DENTRO DO DICIONÁRIO ANINHADO
print(filmsDict["Interstellar"]["genres"])

# 2 - ADICIONAR NOVO ITEM NO DICIONÁRIO ANINHADO
filmsDict["Inception"]["director"] = "Christopher Nolan"
print(filmsDict["Inception"])

# 3 - EXCLUIR UM DICIONÁRIO
del filmsDict["The Dark Knight"]
pp.pprint(filmsDict)