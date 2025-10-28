filmsSet = {"The Conjurering", "Annabelle", "A Maldição da Chorona", "Invocação do Mal", "O Exorcista"}
print(type(filmsSet))

# 1 - BUSCAR O TAMANHO DO SET
print(len(filmsSet))

# 2 - TRUE E 1 SÃO CONSIDERADOS IGUAIS NO SET
exampleSet = {"The Conjurering", 1, True, 6.5}
print(exampleSet)

# 3 - ADD ITENS DE OUTRO SET
filmsSet.update(exampleSet)
print(filmsSet)

# 4 - REMOVER ITENS DO SET
filmsSet.remove(1)
filmsSet.remove(6.5)
print(filmsSet)

# O MAIOR ELEMENTO DO SET

