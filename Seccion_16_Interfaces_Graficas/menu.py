from tkinter import *

# Inicializo la ventana
root = Tk()

# Creacion de la barra superior de los menu
menuBar = Menu(root)
root.config(menu=menuBar)

# Asigno las variables de los nombres a los menú
archivoMenu = Menu(menuBar, tearoff=0)
# Asigno los elementos (Submenu) al menu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=root.quit)


# Asigno las variables de los nombres a los menú
editarMenu = Menu(menuBar, tearoff=0)
editarMenu.add_command(label="Cortar")
editarMenu.add_command(label="Copiar")
editarMenu.add_command(label="Pegar")

# Asigno las variables de los nombres a los menú
ayudaMenu = Menu(menuBar, tearoff=0)
ayudaMenu.add_command(label="Ayuda")
ayudaMenu.add_separator()
ayudaMenu.add_command(label="Acerca de...")

# Dibujar o asigno los nombres en el menú con el metodo en cascada
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editarMenu)
menuBar.add_cascade(label="Ayuda", menu=ayudaMenu)


# Fin de la ventana e inicio del bucle
root.mainloop()