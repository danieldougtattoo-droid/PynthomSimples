class game:
    name = ""
    yearlaunch = 0
    multplayer = False
    note = 0
    def __init__(self, name="", yearlaunch=0, multiplayer=False, note=0):
        self.name = name
        self.yearlaunch = yearlaunch
        self.multplayer = multiplayer
        self.note = note

    def __str__(self):
        return f"Game:{self.name}"

game1 = game("Street Fighter", 1986, False, 9.9)
game2 = game("Mega - MEN", 1988, False, 9.8 )

print("=======Dados do jogo======")
print(f"\nNome do jogo:{game1.name}\nAno de lançamento:{game1.yearlaunch}")
print(f"\nNome do jogo:{game2.name}\nAno de lançamento:{game2.yearlaunch}")