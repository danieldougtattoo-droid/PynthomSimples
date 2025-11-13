# Classe pai (super classe) - generalista
class game:
    total_games = 0 # variável de classe para contar o números de jogos
    def __init__(self, name="", yearlaunch=0, multiplayer=False, note=0):
        self.name = name
        self.yearlaunch = yearlaunch
        self.multplayer = multiplayer
        self.note = note
        game.total_games += 1
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

    def evaluate(self, note):
        self.note += note
        self.evaluators += 1

    def average(self):
        print(f"Média de notas do filme {self.name}:{self.note / self.evaluators}")

# Classe derivada(subclass) - Especializada
class SinglePlayerGame(game):
    def __init__(self, name="", yearlaunch=0, note=0, storeline=""):
        super().__init__(name, yearlaunch, multiplayer=False, note=note)
        self.storeline = storeline

    def thecnical_sheet(self):
        super().thecnical_sheet()
        print(f"Enredo: {self.storeline}\n")

mult_game = game("Street of Rage", 2025, True, 8.6)
mult_game.thecnical_sheet()

sing_game =  SinglePlayerGame("Zelda", 2010, 9.5, "pura emoção")
sing_game.thecnical_sheet()