
from FiguraGeometrica import FiguraGeometrica

from Color import Color

class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):

        FiguraGeometrica.__init__(self, alto=lado, ancho=lado)

        Color.__init__(self, color=color)

    def area(self):

        return self.alto * self.ancho

    def __str__(self):

        return f"Cuadrado -> {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}, Área: {self.area()}"