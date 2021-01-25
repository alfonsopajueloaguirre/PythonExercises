from trabajador import *
import funciones

lista_trabajadores = list()

def menu():
    print("1. Ver trabajadores")
    print("2. Ver trabajadores con IgM")
    print("3. Ver trabajadores con IgG")
    print("4. Ver trabajadores con IgG e IgM")
    print("5. Ver trabajadores sin IgG ni IgM")
    print("6. Porcentaje mujeres infectadas")
    print("7. Porcentaje hombres infectados ")
    print("8. EXIT")
    print()

def fichero():
    lista_trabajadores = list()
    with open('trabajadores.txt', 'r', encoding="utf-8-sig") as fichero:
        lineas = fichero.read().splitlines()
        for i in lineas:
            lista_trabajadores.append(Trabajador(*i.split(' ')))
    return lista_trabajadores

def main():
    lista = fichero()
    datos = funciones.trabajador(lista)
    seguir = 1
    while seguir != 0:
        menu()
        opcion = int(input("Seleccione los datos que quiere ver."))
        if opcion == 1:
            funciones.imprimir_trabajadores(lista)
        elif opcion == 2:
            funciones.imprimir_trabajadores(datos['IgM'])
        elif opcion == 3:
            funciones.imprimir_trabajadores(datos['IgG'])
        elif opcion == 4:
            funciones.imprimir_trabajadores(datos['IgG_IgM'])
        elif opcion == 5:
            funciones.imprimir_trabajadores(datos['Ni_IgG_Ni_IgG'])
        elif opcion == 6:
            print(datos['mujeres'])
            print()
        elif opcion == 7:
            print(datos['hombres'])
            print()
        elif opcion == 8:
            seguir = 0
        else:
            print("Opción incorrecta")
            print()

main()
