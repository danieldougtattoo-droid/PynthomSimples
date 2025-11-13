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

    def evaluate(self, note):
        self.totalevaluate += note
        self.evaluators += 1

    def average(self):
        print(f"Média de notas do filme {self.name}:{self.totalevaluate / self.evaluators}")


game1 = game("Street Fighter", 1986, False, 9.9) 
game2 = game("Mega - MEN", 1988, False, 9.8 )

game1.thecnical_sheet()
game2.thecnical_sheet()
game1.evaluate(9.5)
game1.evaluate(5.9)
game2.evaluate(8.9)
game2.evaluate(9.3)
game1.average()
game2.average()
