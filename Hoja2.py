
def esMayor():
    print("Introduzca su edad: ")
    edad = input()
    if (int(edad)<18):
        print("Es menor de edad")
    else:
        print("Es mayor de edad")

def esTributario():
    noTributa = "No tiene que tributar"
    print("Introduzca su edad: ")
    edad = input()
    if int(edad)<16: 
        print(noTributa)
    else:
        print("Introduzca sus ingresos mensuales: ")
        ingresos = input()
        if int(ingresos)<1000:
            print(noTributa)
        else:
            print("Tiene que tributar")

def esGrupo():
    hombre = "Hombre"
    mujer = "Mujer"
    print("Introduzca su nombre: ")
    nombre = input()
    lista1 = ("ABCEFGHIJKLM")
    letra = nombre[:1]
    resultado = lista1.count(letra)
    print("Introduzca su sexo: Hombre/Mujer")
    sexo = input()
    if ((sexo==mujer)and(resultado==1))or((sexo==hombre)and(resultado==0)):
        print("Grupo A")
    else:
        print("Grupo B")

def IRPF():
    print("Introduzca su renta anual: ")
    renta = input()
    rentaInt = int(renta)
    if rentaInt < 10000:
        print("Tipo del 5%")
    elif rentaInt < 20000:
        print("Tipo del 15%")
    elif rentaInt < 35000:
        print("Tipo del 20%")
    elif rentaInt < 60000:
        print("Tipo del 30%")
    else:
        print("Tipo del 45%")

def capital():
    print("Introduzca cantidad a invertir: ")
    cantidad = input()
    print("Introduzca el interes anual: ")
    interes = input()
    print("Introduzca los años: ")
    años = input()
    resultado = int(cantidad) + (int(cantidad) * int(interes) / 100 * int(años)) 
    print("El capital que obtiene es de " + str(resultado) + " €")

def bonificacion():
    bonificacion = 2400
    inaceptable = 0
    aceptable = 0.4
    meritorio = 0.6
    puntos = float(input("Introduce tu puntuación: "))
    # Clasifiación por niveles de rendimiento
    if puntos == inaceptable:
        nivel = "Inaceptable"
    elif puntos == aceptable:
        nivel = "Aceptable"
    elif puntos >= 0.6:
        nivel = "Meritorio"
    else:
        nivel = ""
    # Mostrar nivel de rendimiento
    if nivel == "":
        print("Esta puntuación no es válida")
    else:
        print("Tu nivel de rendimiento es %s" % nivel)
        print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))


def pizza():
    # Presentación del menú con los tipos de pizza
    print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
    tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
    # Decisión sobre el tipo de pizza
    if tipo == "1":
        print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
        ingrediente = input("Introduce el ingrediente que deseas: ")
        print("Pizza vegetariana con mozzarella, tomate y ", end="")
        if ingrediente == "1":
            print("pimiento")
        else: 
            print("tofu")
    else:
        print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
        ingrediente = input("Introduce el ingrediente que deseas: ")
        print("Pizza no vegetarina con mozarrella, tomate y ", end="")
        if ingrediente == "1":
            print("peperoni")
        elif ingrediente == "2":
            print("jamón")
        else:
            print("salmón")