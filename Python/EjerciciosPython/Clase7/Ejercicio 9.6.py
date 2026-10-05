# Crear la clase Cubo con los atributos, ancho, alto y profuncidad, con un
# metodo calcular_volumne que tendra la fórmula:
#volumen = ancho * altura * profundidad
#que el usuario ingrese los valores.

class Cubo:
    def __init__(self,ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad


ancho= float(input('Ingrese la ancho del cubo: '))
altura= float(input('Ingrese la altura del cubo: '))
profundidad= float(input('Ingrese la profundidad: '))

volumen = ancho * altura * profundidad
print(f'El volumen del cubo: {volumen}')