from cProfile import label
from tkinter import*


# Funciones
def Seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def Resetear():
    opcion.set(None)
    monitor.config(text="")

# Inicio de la aplicacion
root = Tk()

opcion = IntVar()

Radiobutton(root, text="Opcion 1", variable=opcion, value=1, command=Seleccionar).pack()
Radiobutton(root, text="Opcion 2", variable=opcion, value=2, command=Seleccionar).pack()
Radiobutton(root, text="Opcion 3", variable=opcion, value=3, command=Seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Limpiar valores", command=Resetear).pack()

# Fin de la aplicacion
root.mainloop()