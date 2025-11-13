import sys
import os
# Add parent directory to path so we can import modelos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelos import biblioteca


class Biblioteca:
    bibliotecas = []
    def __init__(self, name):
        self.name = name
        self._ativo = False
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.name

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

    @classmethod
    def listar_bibliotecas(cls):
        for bib in cls.bibliotecas:
            print(f"{bib.name} | {bib.ativo}")

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_cidade._ativo = True
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()

print(biblioteca_cidade)
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()