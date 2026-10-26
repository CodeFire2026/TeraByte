
class Persona: # Esta clase hereda de la clase object
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad


    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def __str__(self): # Override = sobreescribir
        return f"Persona [Nombre: {self.get_nombre()}, Edad: {self.get_edad()}]"

class Empleado(Persona): # Esta clase hereda de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.__sueldo = sueldo


    def get_sueldo(self):
        return self.__sueldo


    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo

    def __str__(self): # Override = sobreescribir
        return f"Empleado [ Sueldo: {self.get_sueldo()}] {super().__str__()}"

empleado1 = Empleado('Ariel', 40, 75000)
print("Empleado 1:")
print("Nombre:", empleado1.get_nombre())
print("Edad:", empleado1.get_edad())
print("Sueldo:", empleado1.get_sueldo())
#print(empleado1.nombre) # Asi se imprime sin encapsulamiento
#print(empleado1.edad)
#print(empleado1.sueldo)
# Tarea: encapsular los atributos y agregar los metodos getters and setters
# Crea otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado('Mauro', 30, 50000)
print("\nEmpleado 2")
print("Nombre:", empleado2.get_nombre())
print("Edad:", empleado2.get_edad())
print("Sueldo:", empleado2.get_sueldo())

empleado2.set_nombre('Mauricio')
empleado2.set_edad(26)
empleado2.set_sueldo(60000)

print("\nEmpleado 2 (modificado):")
print("Nombre:", empleado2.get_nombre())
print("Edad:", empleado2.get_edad())
print("Sueldo:", empleado2.get_sueldo())