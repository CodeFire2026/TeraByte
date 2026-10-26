class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property
    def nombre(self):  # Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Setter
        self._nombre = nombre

    @property
    def apellido(self):  # Getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Setter
        self._apellido = apellido

    @property
    def edad(self):  # Getter
        return self._edad

    @edad.setter
    def edad(self, edad):  # Setter
        self._edad = edad


persona1 = Persona2('María', 'López', 30)
persona1.nombre = 'María José'
persona1.apellido = 'Fernández'
persona1.edad = 31
persona1.mostrar_detalles()

persona2 = Persona2('Carlos', 'Pérez', 25)
persona2.nombre = 'Carlos Alberto'
persona2.apellido = 'Ramírez'
persona2.edad = 26
persona2.mostrar_detalles()

persona3 = Persona2('Lucía', 'Martínez', 35)
persona3.nombre = 'Luciana'
persona3.apellido = 'Martínez Gómez'
persona3.edad = 36
persona3.mostrar_detalles()



