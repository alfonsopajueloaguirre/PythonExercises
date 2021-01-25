"""Utilizacion de paradigma estructural: Este modulo es el que se encarga de llamar al resto para dar vida al programa controlando entradas(entrada estandar y llamadas a subprogramas) y salidas(salida estandar). En todos los modulos
se puede ver programacion estructural a traves de bucle if y for, en este en concreto nos valemos de un while para mostrar el menu hasta que el usuario decidad cerrar el programa.  """
import funciones

def main():
    lista_titulaciones = funciones.leer_titulaciones()
    estadisticas = funciones.stat_titulaciones(lista_titulaciones)
    menu = 1
    while menu!=0:
        funciones.mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            funciones.imprimir_titulaciones(lista_titulaciones)
        elif opcion == 2:
            funciones.imprimir_escuelas(lista_titulaciones)
        elif opcion == 3:
            print(estadisticas)
        elif opcion == 4:
            print("Programa terminado")
            menu = 0
        else:
            print("No tengo esa opcion")


main()

