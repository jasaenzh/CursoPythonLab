from cgitb import text
from tkinter import *

# Configurar la raiz
root = Tk()

texto = Text()
texto.pack()
texto.config(width=30, height=10, font=("Consolas",12), padx=15, pady=15, selectbackground="blue")



# Cierro el ciclo del root
root.mainloop()