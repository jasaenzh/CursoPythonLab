from tkinter import *

# Inicializo la ventana
root = Tk()

# Creacion de la barra superior de los menu
menuBar = Menu(root)
root.config(menu=menuBar)

# Asigno las variables de los nombres a los menú
archivoMenu = Menu(menuBar)
editarMenu = Menu(menuBar)
ayudaMenu = Menu(menuBar)

# Dibujar o asigno los nombres en el menú con el metodo en cascada
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editarMenu)
menuBar.add_cascade(label="Ayuda", menu=ayudaMenu)


# Fin de la ventana e inicio del bucle
root.mainloop()