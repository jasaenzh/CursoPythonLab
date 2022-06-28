from cProfile import label
from cgitb import text
from logging import PlaceHolder, root
from tkinter import*

#Creo la funcion Sumar con el metodo get para obtener lo que se digita
def Sumar():
    r.set( float(n1.get()) + float(n2.get()))
    Resetear()

def Restar():
    r.set( float(n1.get()) - float(n2.get()))
    Resetear()

def Producto():
    r.set( float(n1.get()) * float(n2.get()))
    Resetear()

def Resetear():
    n1.set("")
    n2.set("")

#Inicio la aplicacion
root = Tk()
root.config(bd=15)

# Creo las variables
n1 = StringVar()
n2 = StringVar()
r = StringVar()


Label(root, text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack() # Primer numero

Label(root, text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack() # Segundo numero

#Boton Sumar
Label(root, text="").pack()
Button(text="Sumar", command=Sumar).pack()

#Boton Restar
Label(root, text="").pack()
Button(text="Restar", command=Restar).pack()

#Boton Producto
Label(root, text="").pack()
Button(text="Producto", command=Producto).pack()

Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack() # Resultado


#Finalizo la aplicacion
root.mainloop()