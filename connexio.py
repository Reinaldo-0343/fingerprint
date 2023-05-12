import mysql.connector
from mysql.connector import Error

# Estableix la connexió amb la base de dades
try:
    connexio = mysql.connector.connect(
        host='bbdd.g2sapalomera.cat',
        database='nom_de_la_base_de_dades',
        user='ddb202800',
        password='Gr1p0d3.'
    )
except Error as e:
    print(f'Error al connectar amb la base de dades: {e}')
    exit()