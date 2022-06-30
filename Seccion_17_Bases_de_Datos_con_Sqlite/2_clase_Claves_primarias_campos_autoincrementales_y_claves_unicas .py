# Importo la clase
import sqlite3

# abro o creo la conexion
conexion = sqlite3.connect("usuarios_autoincremental.db")

# Inicializo el cursor
cursor = conexion.cursor()

# Sentencias

# Ingreso los registros

# Hago consulta con el condicional WHERE (donde)
cursor.execute("DELETE FROM usuarios WHERE dni='44444444D'")



# Confirmo registro
conexion.commit()

# Cierro la conexion
conexion.close()