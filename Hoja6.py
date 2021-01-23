class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __repr__(self):
        cadena = (
            "Alumno: " + self.nombre + "\n" + 
            "Nota:" + str(self.nota)
        )
        return cadena

    def aprobado(self):
        if self.nota > 5:
            print("Alumno con nombre " + self.nombre + " ha aprobado con un " + str(self.nota))
        else:
            print("Alumno con nombre " + self.nombre + " ha suspendido con un " + str(self.nota))

    alumno1 = Alumno("Juan", 3)
    print(alumno1)
    alumno1.aprobado()
    