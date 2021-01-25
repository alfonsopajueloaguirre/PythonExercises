class Titulacion():
    def __init__(self,nombre,escuela,nivel,creditos,año):
        self.titulacion = nombre
        self.escuela = escuela
        self.nivel = nivel
        self.creditos = creditos
        self.año_implantacion_inicial = año

    def __repr__(self):
        cadena = (
            "Titulacion: " + self.titulacion + "\n" +
            "Escuela: " + self.escuela + "\n" +
            "Nivel: " + self.nivel + "\n" +
            "Creditos: " + self.creditos + "\n" +
            "Años de implantacion: " + self.año_implantacion_inicial 
        )
        return cadena
    
    