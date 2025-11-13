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
        self.totalevaluate = 0
        self.evaluators = 0

    def __str__(self):
        return f"Game:{self.name}"

    def thecnical_sheet(self):
        print("====== Dados do jogo ======")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.yearlaunch}")
        print(f"Modo multiplayer?: {self.multplayer}")
        print(f"Nota do jogo: {self.note}\n")

class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.game = []

    def add_game(self, game):
        self.game.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in (self.game))
        num_game = len(self.game)
        if num_game == 0:
            print(f"O studio {self.name} ainda não lançou jogos")
        else:
            average = total_notes / num_game
            print(f"A avaliação de jogos do studio {self.name}: {average:.2f}")

game1 = game("Street Fighter", 1986, False, 9.9) 
game2 = game("Mega - MEN", 1988, False, 9.8 )
game3 = game("Birdoland", 2025, False, 6.6)

studio = GameStudio("Awesone Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality

for game in studio.game:
    game.thecnical_sheet()