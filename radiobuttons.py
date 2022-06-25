from tkinter import*

# Inicio de la aplicacion
root = Tk()

opcion = IntVar()

Radiobutton(root, text="Opcion 1", variable=opcion).pack()
Radiobutton(root, text="Opcion 2", variable=opcion).pack()
Radiobutton(root, text="Opcion 3", variable=opcion).pack()

# Fin de la aplicacion
root.mainloop()