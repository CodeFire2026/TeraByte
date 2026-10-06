class Persona: #Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llaa metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo está encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad} la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona("Claudio", "Olima", 38758982, 32) # Necesitamos enviar argumentos
print(f'El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 47852963, 45)
print(f'El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} Su Edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

# Los atributos son: Caracteristicas
# Los metodos son: El comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automática
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error
persona1.telefono = "44545445"
print(f"Este es el teléfono de {persona1.nombre}: {persona1.telefono}") # Hemos creado un atributo de un objeto

# print(persona1.telefono) el objeto persona2 no tiene ese atributo, da error
persona3 = Persona("Rogelio", "Romero", 29452589, 22, "Telefono", "2613524106", "Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura=1.83, Peso=105, CFavorita="Azul", Auto="Citroen", Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) # Esto no se debe utilizar(esta encapsulado), esto dice que lo desconocemos python
# persona3.__nombre # Esta totalmente encapsulado

