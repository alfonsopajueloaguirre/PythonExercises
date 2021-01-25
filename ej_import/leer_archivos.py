from persona import *
'''Aquí podemos importar toda la info de persona ya que en el archivo persona.py
no se importa nada que no se vaya a usar. Aun así, es recomendable no hacer esto
'''

def leer_personas(ruta):
    personas = list()
    with open(ruta, 'r', encoding='utf-8-sig') as f:
        lineas = f.read().splitlines()
        for linea in lineas:
            personas.append(Persona(*linea.split(' ')))
    return personas