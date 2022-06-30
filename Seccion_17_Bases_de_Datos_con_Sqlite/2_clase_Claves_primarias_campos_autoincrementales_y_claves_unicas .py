# Importo la clase
import sqlite3

# abro o creo la conexion
conexion = sqlite3.connect("productos.db")

# Inicializo el cursor
cursor = conexion.cursor()

# Sentencias

# Creo la tabla
cursor.execute('''
CREATE TABLE productos(
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_producto VARCHAR (100) NOT NULL,
    marca VARCHAR (50) NOT NULL,
    precio FLOAT NOT NULL
    )
''')

# Confirmo registro
conexion.commit()

# Cierro la conexion
conexion.close()