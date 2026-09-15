# Desenpaquetado de listas o list unpacking
def show(name, lastname):
    print(name+' '+lastname)
person = ["Claudio", "Olima"]
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la fincion
show(*person) # Esto es lo ismo que lo anterior pero lo pasamos todo junto
person2 = ("Osvaldo", "Giordanini") # Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastname": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejjecutar el else
for n in numbers:
    print(n)
    if n ==  3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

# List comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P']# Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg" },
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"]== "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a traves del canal de Youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

# La palabra return en funciones
# Creamos una funcion para sumar

def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
# print(f"El resultado de la suma es: {resulado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

# Argumentos, variables en funciones
def ListarNombres(*nombres): # Normalmente se utiliza: *Args
    for nombre in nombres: # Se va a Convertir en una tupla
        print(nombre)
ListarNombres("Lucas", "Jose", "Claudio", "Rosa", "Maria")
ListarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcelo", "Carlos")


