""" Funciones de Ayuda """

from cgitb import text
import os
import platform

# Funcion para limpiar terminal
def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Funcion de ayuda para condicionar el ingreso de datos min y max
def input_text(min_length, max_length):
    while True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text