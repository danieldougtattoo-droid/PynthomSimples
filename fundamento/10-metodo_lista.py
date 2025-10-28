filmList = ["The Conjurering", "Annabelle", "A Maldição da Chorona", "Invocação do Mal", "O Exorcista"]

# - Tamanho da lista
print(len(filmList))

# - Recuperar um item da lista pelo nome
print(filmList.index("Invocação do Mal"))

# - Adicionar um item no final da lista
filmList.append("Atividade Paranormal")
print(filmList)

# - Ordenação da lista
filmList.sort()
print(filmList)

# - Copiar os itens de uma lista para a outro
filmCopy = filmList.copy()
filmCopy.remove("Atividade Paranormal")
print(filmCopy)