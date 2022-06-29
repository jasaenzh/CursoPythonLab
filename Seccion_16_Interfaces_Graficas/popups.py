from logging import root
from tkinter import*
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from turtle import title
from tkinter import filedialog as FileDialog



# Inicializo la ventana
root = Tk()

def Ejecutar():
    fichero = FileDialog.asksaveasfile(title="Guardar archivo", mode="a", defaultextension=".txt")
    if fichero is not None:
        fichero.write("Hola mundo")
        fichero.close()

Button(root, text="Ejecutar", command=Ejecutar).pack()


# Finalizo la ventana y comieza el bucle
root.mainloop()