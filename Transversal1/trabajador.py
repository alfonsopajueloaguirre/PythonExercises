class Trabajador():
    def __init__(self,nombre,apellido_1,apellido_2,edad,sexo,IgM,IgG):
        self.nombre_trabajador = nombre
        self.apellido_trabajador_1 = apellido_1
        self.apellido_trabajador_2 = apellido_2 
        self.edad_trabajador = edad
        self.sexo_trabajador = sexo
        self.IgM_trabajador = IgM
        self.IgG_trabajador = IgG

    def __repr__(self):
        cadena = (
            "Nombre del trabajador: " + self.nombre_trabajador + '\n' +
            "Primer apellido del trabajador: " + self.apellido_trabajador_1 + '\n' +
            "Segundo apellido del trabajador: " + self.apellido_trabajador_2 +'\n' +
            "Edad del trabajador: " + self.edad_trabajador + '\n' +
            "Sexo del trabajador: " + self.sexo_trabajador + '\n' +
            "IGM del trabajador: " + self.IgM_trabajador + '\n' +
            "IGG del trabajador: " + self.IgG_trabajador + '\n'
            )
        return cadena