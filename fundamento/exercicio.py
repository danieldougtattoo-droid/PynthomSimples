


# LEIA O NOME DE um PRODUTOS E SEUS RESPECTIVOS PREÇOS.
product1 = input("Digite o nome do primeiro produto")
price1 = float(input("Digite o preço do primeiro produto"))
product2 = input("Digite o nome do segundo produto")
price2 = float(input("Digite o preço do segundo produto"))

# ARMAZENE OS DADOS EM UM DICIONÁRIO ONDE A CHAVE SERA O NOME DO PRODUTO E O VALOR É O PREÇO(FLOAT).
productsDict = {
    product1: price1,
    product2: price2
}
print(productsDict)
print(max(productsDict, key=productsDict.get))

# imprima a media de preço dos produtos no dicionario.
avarage_price = sum(productsDict.values()) / len(productsDict)
print(f"A média de preço dos produtos é: {avarage_price:.2f}")
