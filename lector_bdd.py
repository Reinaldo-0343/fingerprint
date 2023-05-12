import mysql.connector

# Conectar a la base de datos
connexio = mysql.connector.connect(
    host="localhost",
    user="usuarii",
    password="contrasenya",
    database="sistema_fichatge"
)

# Obtener un cursor
cursor = connexio.cursor()

# Leer la huella dactilar
emprenta = leer_huella_dactilar()

# Convertir la huella en bytes
emprenta_bytes = bytes(emprenta)

# Insertar la huella en la base de datos
consulta = "INSERT INTO <nombre_de_la_tabla> (usuario, huella_dactilar) VALUES (%s, %s)"
valores = ("usuario1", huella_bytes)
cursor.execute(consulta, valores)

# Guardar los cambios
connexio.commit()

# Cerrar la conexión
connexio.close()
