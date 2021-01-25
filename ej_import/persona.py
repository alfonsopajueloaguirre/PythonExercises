class Persona():
    def __init__(self, nombre, apellido, tula):
        self.nombre = nombre
        self.apellido = apellido
        self.tula = tula


    def __repr__(self):
        return (
            self.nombre + '\n' +
            self.apellido + '\n' +
            self.tula + '\n'
        )