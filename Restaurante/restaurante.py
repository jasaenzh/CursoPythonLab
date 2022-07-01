import sqlite3
from time import process_time_ns

# Creo la funcion para crear la BD

def  crear_bd():
    # Creo la conexion
    conexion = sqlite3.connect("restaurante.db")
    # Creo el cursor
    cursor = conexion.cursor()

    try:
        # Creo las tabla Categoria
        cursor.execute('''CREATE TABLE categoria(
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla Categoria ya existe")
    else:
        print("La base de datos se ha creado correctamente")


    try:
        # Creo tabla Plato
        cursor.execute('''CREATE TABLE plato(
            id_plato INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR (100) UNIQUE NOT NULL,
            id_categoria INTEGER NOT NULL,
            FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria))''')
    except sqlite3.OperationalError:
        print("La tabla Plato ya existe")
    else:
        print("La base de datos se ha creado correctamente")

    # Cierro la conexion
    conexion.close()

def agregar_categoria():
    categoria = input("\nNombre de la nueva categoria: \n>")

    # Creo la conexion
    conexion = sqlite3.connect("restaurante.db")
    # Creo el cursor
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("\nLa categoria '{}' ya existe.".format(categoria))
    else:
        print("\nSe ha creado la Categoria '{}'".format(categoria))

        conexion.commit()
        conexion.close()

def agregar_plato():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("\nSelecciona una categoria para añadir el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

    plato = input("Nombre del nuevo plato\n >")

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print("\nEl plato '{}' ya existe.".format(plato))
    else:
        print("\nSe ha creado El Plato '{}'".format(plato))

    conexion.commit()
    conexion.close()

def mostrar_menu():
    # Creo la conexion
    conexion = sqlite3.connect("restaurante.db")
    # Creo el cursor
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM plato WHERE id_categoria={}".format(categoria[0]))
        for plato in platos:
            print("\t{}".format(plato[1]))

    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input("\n[--- MENU ---] \n[1] Agregar una categoria \n[2] Agregar Plato \n[3] Mostrar Menu \n[4] Salir del programa \nIntroduce la Opcion: ")

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        print("Hasta la proxima")
        break
    else:
        print("Opción incorrecta")