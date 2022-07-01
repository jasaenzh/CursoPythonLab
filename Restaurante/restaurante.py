import sqlite3

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
    categoria = input("Nombre de la nueva categoría: \n>")

    # Creo la conexion
    conexion = sqlite3.connect("restaurante.db")
    # Creo el cursor
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))

    conexion.commit()
    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input("\nIntroduce un opción: \n[1] Agregar una categoría \n[2] Salir del programa \nIntroduce la Opcion: ")

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        break
    else:
        print("Opción incorrecta")