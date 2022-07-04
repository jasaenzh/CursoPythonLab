#coding=utf-8

""" Administrador de clientes """

from http import client
import re
import helpers
import doctest

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

    for i, client in enumerate(clientes):
        if client ['dni'] == dni:
            show(client)
            return i, client
    print ("No se ha encontrado ningun cliente con este DNI")


# Funcion para validar añadir cliente mediante DNI
def is_valid(dni):
    """
    >>>is_valid('48H')
    False
    >>>is_valid('X82')
    False
    >>>is_valid('21A')
    True
    """

    # Comprueba que el dni empieza con un patron
    if not re.match('[0-9]{2}[A-Z]',dni):
        return False

    for cliente in clientes:
        if cliente['dni']==dni:
            return False

    return True


# Funcion para añadir cliente
def add():
    client = dict()

    print("Introduce nombre (De 2 a 30 Caracteres)")
    client['nombre'] = helpers.input_text(2,30)

    print("Introduce apellido (De 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2, 30)

    while True:
        print("Introduce DNI (2 numeros y 1 caracter en mayuscula)")
        dni = helpers.input_text(3,3)
        if is_valid(dni):
            client['dni']=dni
            break
        print("DNI incorrecto o en uso")

    clientes.append(client)
    return client


# Funcion para editar cliente
def edit():

    i, client = find()

    if client:
        print(f"Introduce nuevo nombre ({client['nombre']})")
        clientes[i]['nombre'] = helpers.input_text(2, 30)
        print(f"Introduce nuevo apellido ({client['apellido']})")
        clientes[i]['apellido'] = helpers.input_text(2, 30)
        return True
    return False

# Funcion para borrar cliente
def delete():
    i, client = find()
    if client:
        client = clientes.pop(i)
        return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()