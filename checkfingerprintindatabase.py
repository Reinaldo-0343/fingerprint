import mysql.connector
from mysql.connector import Error
from Adafruit_Fingerprint import Adafruit_Fingerprint

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



# Inicialitza el lector d'empremtes dactilars
f = Adafruit_Fingerprint()

# Captura l'empremta dactilar
print('Poseu el dit al lector...')
while f.get_image() != f.FINGERPRINT_OK:
    pass

# Converteix l'empremta dactilar a una cadena de bytes
empremta = f.image_2_tz()


# Consulta la base de dades per buscar l'empremta dactilar
consulta = "SELECT usuari, empremta FROM empremtes"
cursor = connexio.cursor()
cursor.execute(consulta)
resultat = cursor.fetchall()

# Verifica si l'empremta dactilar coincideix amb alguna registrada
for fila in resultat:
    if f.verify(empremta, fila[1]):
        print(f'Usuari identificat: {fila[0]}')
        break
else:
    print("No s'ha reconegut cap empremta dactilar")
