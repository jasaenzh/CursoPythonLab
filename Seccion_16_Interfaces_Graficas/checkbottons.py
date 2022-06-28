from cgitb import text
from logging import root
from struct import pack
from tkinter import *

# inicio de la ventana
root = Tk()
root.title("Cafetería")
root.config(bd=15)

# Funciones
def Seleccionar():
    cadena = ""
    if(leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if(azucar.get()):
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"
    
    monitor.config(text=cadena)




# Declaro las variables 1 es Si, 0 es No

leche = IntVar()
azucar = IntVar()

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")


frame = Frame(root)
frame.pack(side="left")

Label(frame, text="Como quieres el cafe?").pack()

Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=Seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=Seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()



# Fin de la ventana y blucle
root.mainloop()