from Examen.titulacion import *
def imprimir_titulaciones(lista_titulaciones):
    for i in lista_titulaciones:
        print(i)

def stat_titulaciones(lista_tituaciones):
    pass

def mostrar_menu():
    print("1. Ver todas las titulaciones")
    print("2. Ver titulaciones por escuela")
    print("3. Mostrar estadisticas")
    print("4. Salir")

def leer_titulaciones():
    lista_titulaciones = []
    with open('titulaciones.txt', 'r', encoding="utf-8-sig") as fichero:
        lineas = fichero.read().splitlines()
        for i in lineas:
            lista_titulaciones.append(Titulacion(*i.split(' ')))
    return lista_titulaciones