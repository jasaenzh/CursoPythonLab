# Importo la clase
import sqlite3

# abro o creo la conexion
conexion = sqlite3.connect("usuarios.db")

# Inicializo el cursor
cursor = conexion.cursor()

# Sentencias

## Creo Tabla
cursor.execute('''
CREATE TABLE usuarios
    (
        dni VARCHAR(9) PRIMARY KEY,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
''')

# Insertar varios registros se deben hacer como tuplas
usuarios = [
    ('11111111A','Jhony Saenz',37,'jsaenz@correo.com'),
    ('22222222B','Andres Ortiz',38,'andrescarlos@correo.com'),
    ('33333333C','Luz Maria',45,'luzmaria@correo.com'),
    ('44444444D','Jhony Saenz',37,'jsaenz@correo.com')
]

cursor.executemany("INSERT INTO usuarios VALUES(?,?,?,?)",usuarios)

# Confirmo registro
conexion.commit()

# Cierro la conexion
conexion.close()