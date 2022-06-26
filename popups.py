from logging import root
from tkinter import*
from tkinter import messagebox as MessageBox

# Inicializo la ventana
root = Tk()

def Ejecutar():
    resultado = MessageBox.askretrycancel("Reintentar", "No se pudo conectar")
    if resultado == True:
        root.destroy()

Button(root, text="Ejecutar", command=Ejecutar).pack()


# Finalizo la ventana y comieza el bucle
root.mainloop()