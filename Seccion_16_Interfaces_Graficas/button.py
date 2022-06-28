from logging import root
from tkinter import *

def saludar():
    print ("Esto es un saludo")

def crear_Label():
    Label(root, text="Label creada desde el boton").pack()

#Inicio la aplicacion
root = Tk()

Button(root, text="Clic aca", command=crear_Label).pack()

#Cierro la aplicacion
root.mainloop()