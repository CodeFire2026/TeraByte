
from FiguraGeometrica import FiguraGeometrica

from Color import Color


class Rectangulo(FiguraGeometrica, Color):

    def __init__(self, alto, ancho, color):

        FiguraGeometrica.__init__(self, alto=alto, ancho=ancho)

        Color.__init__(self, color=color)
    

    def area(self):

        return self.alto * self.ancho

    def __str__(self):

        return f"Rectangulo -> {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}, Área: {self.area()}"