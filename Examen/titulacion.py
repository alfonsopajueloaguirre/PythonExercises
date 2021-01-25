
"""Utilizacion del paradigma orientado a objetos: A la hora de gaurdar los datos leidos de un fichero es necesario crear una estructura de datos para contenerlo, consultarlo y editarlo.
Gracias a loas atributos podemos guardar varios tipos de informacion de un mismo objeto lo que nos beneficiara a la hora de obtener las estadisticas.
Este modulo sera principalemte utilizado por el de funciones donde se trabajara con otro tipo de paradigma de programacion """
class Titulacion():
    def __init__(self,nombre,escuela,nivel,creditos,año):
        self.titulacion = nombre
        self.escuela = escuela
        self.nivel = nivel
        self.creditos = creditos
        self.año_implantacion_inicial = año

    def __repr__(self):
        cadena = (self.titulacion + " " + self.escuela + " " + self.nivel + " " + self.creditos + " " + self.año_implantacion_inicial)
        return cadena