"""
Fatorial de um numero
1-> 1 * 1 = 1
2-> 2 * 1 = fatorial(1) = 2
3-> 3 * 2 * 1 = 6
"""

# 1 - Numero fatorial
def fatorial(num):
  if num == 1:
     return 1
  else:
    return(num * fatorial(num -1))
number = int(input("Digite seu numero para o fatorial:\n"))
print(f"O fatorial de {number} é {fatorial(number)}")

# 2 - Soma total de um numero
def total_sum(num):
    if num == 1:
       return 1
    else:
        return(num + total_sum(num -1)) 

number = int(input("Digite o numero para soma:\n"))
print(f"A soma total de {number} é {total_sum(number)}")