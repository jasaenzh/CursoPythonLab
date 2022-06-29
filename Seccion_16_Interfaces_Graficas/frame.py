# Importo los metodos
from logging import root
from platform import release
from tkinter import *
from turtle import width

# Inicio la aplicacion
root = Tk()
root.title("Frame")
root.iconbitmap("hola.ico")
root.resizable(1,1)

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="green")
frame.config(bd=25)
frame.config(relief="sunken")



# Bucle de la aplicacion
root.mainloop()