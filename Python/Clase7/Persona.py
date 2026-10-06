class Persona:

   def __init__(self, nombre, apellido, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
       self.nombre = nombre
       self.apellido = apellido
      # self._dni = dni #Este atributo esta encapsulado
       self.edad = edad
       self.args = args
       self.kwargs = kwargs

   def mostrar_detalle(self):# self es iguala this
       print(f'La clase Persona tiene los siguiente datos: {self.nombre} {self.apellido} {self.edad}, La dirección es : {self.args}, Los datos importantes son: {self.kwargs}')


persona1 = Persona('Ariel', 'Bentacud', 40,) #Necesitamos enviar argumentos
#print(persona1.nombre) #Tarea: hacer el print igual que co el objeto 2
#print(persona1.apellido)
#print(persona1.edad)
#persona1 = Persona('Ariel', 'Bentacud', 40)
print(f'El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')
persona2 = Persona('Osvaldo', 'Giodadini', 45) #Necesitamos argumentos
print(f'El objeto2 de la clase persona : {persona2.nombre} {persona2.apellido}Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')


#Los atributos caracteristicas
#Los metodos son el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

#Persona.mostrar_detalle() #Debemos pasarle una referencia para el self o dara error
persona1.telefono = '444455552'
print(persona1.telefono)
print(f'Este es el teléfono: {persona1.nombre} {persona1.telefono}')# Hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error
persona3 =Persona('Rogelio', 'Romero',  22,23345656, 'Telefono', '26144445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura =  '1.83', Peso = 105, CFavorito='Azul',Auto ='Citroen', Modelo =2021)
persona3.mostrar_detalle()
#perosna3.__nombre # esta totalmente encapsulado

#print(persona3._dni)esto no se debe utilizar en python (esta encapsulado), esto dice que lo desconoce
#persona4 = Persona( 'Mario', 'Mendoza', 24, 'Telefono', '2604645327', 'Calle Gral.Roca', 1020, 'Manzana', 2, 'Casa', 3, Altura = '1,70', Peso = 80, CFavorito = 'Verde', Auto = 'Chevrolet', modelo = 2020)
#persona4.mostrar_detalle()