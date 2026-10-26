
class FiguraGeometrica:

    def __init__(self, alto, ancho):

        self._alto = alto
        
        self._ancho = ancho

    @property

    def alto(self):

        return self._alto

    @alto.setter

    def alto(self, alto):
        self._alto = alto


    @property
    
    def ancho(self):

        return self._ancho
    

    @ancho.setter

    def ancho(self, ancho):

        self._ancho = ancho

    def __str__(self):

        return f"FiguraGeometrica [Alto: {self._alto}, Ancho: {self._ancho}]"