RUTA_DATOS = "Transversal/datos.txt"
RUTA_RESULTADOS = "Transversal/resultados.txt"
class Pais():
    def __init__(self, nombre, lista_jugador):
        self.nombre = nombre
        self.lista_jugador = lista_jugador

class Jugador():
    def __init__(self, nombre, apellido, edad, mano):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mano = mano

class Grupo():
    def __init__(self, letra, lista_resultados):
        self.letra = letra
        self.lista_resultados = lista_resultados

def leer_datos():
    try:
        with open(RUTA_DATOS, 'r', encoding='utf-8-sig') as fichero:
            lineas = fichero.read().splitlines()
            paises = []
            for linea in lineas:
                campos = linea.split(' ')
                nombre_pais = campos.pop(0)
                jugadores = []
                for i in range(5):
                    jugadores.append(Jugador(*campos[i*4:i*4+4]))
                paises.append(Pais(nombre_pais, jugadores))
            return paises
    except:
        print("Error no se encuentra el archivo de datos.txt")

def leer_resultados():
    try:
        with open(RUTA_RESULTADOS, "r", encoding="utf-8-sig") as fichero:
            lineas = fichero.read().splitlines()
            resultados = []
            for linea in lineas:


