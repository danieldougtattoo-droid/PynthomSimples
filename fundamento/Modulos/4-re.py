import re


text = "Udemy - uma plataforma com muitos cursos"

# 1- Índici inicial e final de palavra
# O r significa uma row string(uma string bruta)

math = re.search(r"uma plataforma", text)
print(f"Índice inicial: {math.start()}")
print(f"Índice inicial: {math.end()} ")

# 2- Buscando o índice que possue o ponto
site = 'http:// udemy.com'
math = re.search(r'\.', site)
print(math)

# 3- Buscando uma lista de caracteres dentro de uma frasa
pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

# 4- Verificando o ínicio de uma string
rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos aprender']
for f in phrases:
     if re.match(rule, f):
        print(f'Corresponde: {f}')
     else:
        print(f'Não corresponde: {f}')

# 5 - Verificando o final de uma string
rule_end = r'!$'
phrase2 = 'O dia está lindo!' 
match = re.search(rule_end, phrase2)
if match:
    print('Sim corresponde')
else:
        print('Não corresponde')




