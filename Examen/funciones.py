"""Utilizacion del paradigma funcional: En este modulo se recogen todas las funciones y subprogramas que seran utilizados por un modulo mas general, el conocido main.
Estas funciones se apoyan en el objeto titulaciones trabajando con sus atributos ademas de contar con subfunciones propias como el caso de imprimir escuelas. Es un paradigma muy util
sobre todo cuando necesitas repetir mucho una funcionalidad como mostrar el menu en un programa hasta qeu este se cierra """
from titulacion import *
def imprimir_titulaciones(lista_titulaciones):
    for i in lista_titulaciones:
        print(i)
    print()

def imprimir_escuelas(lista_titulaciones):
    titulaciones = ["FCS", "FCJS", "ETSII", "ESCET", "ETSIT", "FCC", "EID", "EMO"]
    def dividir(titulacion):
        resultado = list()
        for i in lista_titulaciones:
            if i.escuela == titulacion:
                resultado.append(i.titulacion)
        return resultado
        
    for nombre in titulaciones:
        print(nombre)
        print(dividir(nombre))
        print()

def stat_titulaciones(lista_titulaciones):
    grados = list()
    masters = list()
    doctorados = list()
    implantaciones_2009 = list()
    titulaciones_ETSII = list()
    porcentaje_ETSII = list()

    for i in lista_titulaciones:
        if i.nivel == 'Grado':
            grados.append(i)
        elif i.nivel =="Máster":
            masters.append(i)
        else:
            doctorados.append(i)
        
        if i.año_implantacion_inicial == '2009':
            implantaciones_2009.append(i)

        if i.escuela == "ETSII":
            titulaciones_ETSII.append(i)

    total = len(grados) + len(masters) + len(doctorados)
    porcentaje_grados = round(len(grados) / total*100,1)
    porcentaje_masters = round(len(masters) / total*100,1)
    porcentaje_doctorados = round(len(doctorados) / total*100,1)
    porcentaje_ETSII = round(len(titulaciones_ETSII) / total*100,1)

    cadena = (
        "Total de titulaciones de la universidad: " + str(total) + "\n" +
        "% de titulaciones de Grado: " + str(porcentaje_grados) + "%" + "\n" +
        "% de titulaciones de Master: " + str(porcentaje_masters) + "%" + "\n" +
        "% de titulaciones de Doctorado: " + str(porcentaje_doctorados) + "%" + "\n" +
        "Número de titulaciones implantadas en 2009: " + str(len(implantaciones_2009)) + "\n" +
        "Número de titulaciones de la ETSII: " + str(len(titulaciones_ETSII)) + "\n" +
        "% de titulaciones de la ETSII respecto a la URJC: " + str(porcentaje_ETSII) + "%" + "\n"
    )
    return cadena

def mostrar_menu():
    print("1. Ver todas las titulaciones")
    print("2. Ver titulaciones por escuela")
    print("3. Mostrar estadisticas")
    print("4. Salir")
    print()

def leer_titulaciones():
    lista_titulaciones = []
    with open('titulaciones.txt', 'r', encoding="utf-8-sig") as fichero:
        lineas = fichero.read().splitlines()
        for i in lineas:
            lista_titulaciones.append(Titulacion(*i.split(' ')))
    return lista_titulaciones