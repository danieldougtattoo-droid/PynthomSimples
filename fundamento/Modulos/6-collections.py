from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Lista de frutas (contagem)
fruits = ["Maça", "Banana", "Uva", "Pêra", "Banana",
          "Uva", "Maça", "Banana", "Laranja",
          "Abacaxi", "Tangerina", "Uva", "Pera", "Banana"]
print(fruits)
print(Counter(fruits))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("fifa 25", 90.50, 9.9)
g2 = game("O massacre da serra eletrica", 300, 10.0)
print(g1)
print(g2)

# 3 - Ordenando dicionários
students = {"Pedro": 25, "Ana": 22, "Jáco": 26, "Pipe": 18}
a = sorted(students.items(), key = itemgetter(0))
print(a)

# 4 - Utilizando uma fila em ambas as estremidades
dec = deque([20, 40, 60, 80])
dec.appendleft(10)
print(dec)
dec.append(90)
print(dec)
dec.popleft()
dec.pop

print(dec)