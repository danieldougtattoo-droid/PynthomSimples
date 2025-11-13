class game:
    name = ""
    yearlaunch = 0
    multplayer = False
    note = 0

    # Primeiro jogo
game1 = game()
game1.name = "Street Fighter"
game1.yearlaunch = "1986"
game1.multplayer = False
game1.note = 9.9

# Segundo jogo
game2 = game()
game2.name = "Mega - Men"
game2.yearlaunch = "1988"
game2.multplayer = False
game2.note = 9.9

print("=======Dados do jogo======")
print(f"\nNome do jogo:{game2.name}\nAno de lançamento:{game2.yearlaunch}")