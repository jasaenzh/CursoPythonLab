from cProfile import label
from tkinter import *

# Configuracion rainz
root = Tk()

#Entry
label = Label(root, text="Nombre muy largo")
label.grid(row=0, column=0 , sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="disabled")

label2 = Label(root, text="Contraseña")
label2.grid(row=1,column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1,column=1, padx=5, pady=5,)
entry2.config(justify="right", state="normal", show="*")

# Bucle (cierre) de la aplicacion 
root,mainloop()