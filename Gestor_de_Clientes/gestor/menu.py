# coding=utf-8

""" Menú del programa """

import helpers
import manager

def loop():
    while True:

        # Limpiar la terminal
        helpers.clear()

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir      ")

        option = input("> ")

        # Limpiar la terminal
        helpers.clear()

        if option == '1':
            print("Listando los clientes... \n")
            manager.show_all()
        if option == '2':
            print("Mostrando los clientes... \n")
            manager.find()
        if option == '3':
            print("Añadiendo los clientes... \n")
            manager.add()
            print("\nCliente añadido correctamente")
        if option == '4':
            print("Modificando los clientes... \n")
            manager.edit()
            print("Cliente modificado correctamente\n")
        if option == '5':
            print("Borrando los clientes... \n")
            if manager.delete():
                print("Cliente borrado correctamente\n")
            print("Cliente borrado correctamente\n")
        if option == '6':
            print("Saliendo... \n")
            break

        input("\nPresiona ENTER para continuar..")