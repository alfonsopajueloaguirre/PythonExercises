from leer_archivos import leer_personas
'''Se importa solo el método que queremos porque en leer_archivos se hace un
import de la clase persona, que no nos interesa en este archivo
'''

ruta = 'ej_import/personas.txt'
l_personas = leer_personas(ruta)

print(l_personas)