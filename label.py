# Importo los metodos
from logging import root
from platform import release
from tkinter import *
from turtle import width

# Configuración de la raiz
root = Tk()

# Atributos
root.title("Label")
root.iconbitmap("hola.ico")
root.resizable(1,1)

# Label
label = Label(root, text="Hola Mundo!").pack(anchor='nw')
label = Label(root, text="Otra etiqueta!").pack(anchor='center')
label = Label(root, text="Ultima etiqueta!").pack(anchor="se")




# Bucle de la aplicacion
root.mainloop()