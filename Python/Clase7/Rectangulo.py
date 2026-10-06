"""
Crear una clase llamada Rectángulo, debe tener 2 atributos: altura y base
el nombre del método será calcular el área utilizando la fórmula:
area = base * altura. Pero la base y la altura deber ser ingresadas
por el usuario y los objetos deber ser tres
"""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Método para calcular el área
    def area(self):
        return self.base * self.altura

# Ingresamos los datos del primer rectángulo
base1 = float(input("Ingrese la base del rectángulo 1: "))
altura1 = float(input("Ingrese la altura del rectángulo 1: "))
rectangulo1 = Rectangulo(base1, altura1)

# Ingresamos los datos del segundo rectángulo
base2 = float(input("Ingrese la base del rectángulo 2: "))
altura2 = float(input("Ingrese la altura del rectángulo 2: "))
rectangulo2 = Rectangulo(base2, altura2)

# Ingresamos los datos del tercer rectángulo
base3 = float(input("Ingrese la base del rectángulo 3: "))
altura3 = float(input("Ingrese la altura del rectángulo 3: "))
rectangulo3 = Rectangulo(base3, altura3)

# Imprimimos las áreas de los rectángulos
print("Área del rectángulo 1:", rectangulo1.area())
print("Área del rectángulo 2:", rectangulo2.area())
print("Área del rectángulo 3:", rectangulo3.area())