PrimeiroNome = input("Digite seu nome:/n ")
SegundoNome = input("Digite seu sobrenome:/n")

nomeformatado = f"{SegundoNome} {PrimeiroNome}"
print(nomeformatado)
# Exercício 2

texto = "Python é muito interessante"
palavras = texto.split()
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)
# Exercício 3

# Remova o espaço e deixe tudo em mínusculo
texto1 = "arara"
texto2 = "python"

texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

# Verificar se o texto original é igual ao seu reverso
palíndromo1 = texto1_format == texto1_format[::-1]
palíndromo2 = texto2_format == texto2_format[::-1]

print(palíndromo1)
print(palíndromo2)


# Gere um código que leia nome e 3 notas e mostre a média
name = input("Digite seu nome:\n")
note1 = float(input("Digite a primeira nota:\n"))
note2 = float(input("Digite a segunda nota:\n"))
note3 = float(input("Digite a terceira nota:\n"))
average = (note1 + note2 + note3) / 3
print(f"A média de {name} é: {average:.2f}")



