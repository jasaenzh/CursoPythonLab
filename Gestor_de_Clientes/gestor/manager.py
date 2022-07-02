#coding=utf-8

""" Administrador de clientes """

clientes = []

# Añadimos mock data 
marta = {'nombre':'Marta', 'apellido':'Peréz', 'dni':'15J'}
clientes.append(marta)

# No hace falta crear la variable
clientes.append({'nombre':'Manolo', 'apellido':'Lopez', 'dni':'48H'})
clientes.append({'nombre':'Ana', 'apellido':'Garcia', 'dni':'28Z'})

def show(client):
    print(f"{client['dni']}: {client['nombre']} {client['apellido']}")

def show_all():
    for client in clientes:
        show(client)

def find ():

    dni = input("Introduce el DNI del cliente\n>")

    for client in clientes:
        if client ['dni'] == dni:
            show(client)
            return client

    print ("No se ha encontrado ningun cliente con este DNI")