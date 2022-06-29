# Importo el modulo para la conexion a la base de datos

import sqlite3

# Creando conexion a la base de datos, si no existe se creara automaticamente, se debe de asignar a una variable
conexion = sqlite3.connect("ejemplo.db")

# Creo el cursor
cursor = conexion.cursor()

# Mostrar todos los registros

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

# Confirmar registro
conexion.commit()

# Cierro la conexion
conexion.close()