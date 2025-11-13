from _typeshed import StrOrBytesPath
from logging import shutdown
import os

# 1 - retornar a apasta atual
print(os.getcwd())

# 2- Listar arquivos e pastas
print(os.listdir())

# 3- Versão sistema operacional (os)
os.system('ver')

# 4- Configurações da máquina
os.system("sisteminfo")

# 5- Limpar a tela do terminal
os.system("cls")

# 6 - Desligar o computador
# os.system("shutdow / s")
# os.system("shutdow / s /t 0")
os.system('shutdow /a')

def turn_off_one_hour():
    os.system('shutdow /s /t 3600')

def turn_half_an_hour():
    os.system('shutdow /s /t 1800')

def cancel_shut(): 
    os.system('shutdow /a')