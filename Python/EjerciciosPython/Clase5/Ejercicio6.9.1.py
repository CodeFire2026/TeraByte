# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizándolo argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos.

def suma_valores(*args: int):
    return sum(args)
print(f"La suma de los valores es: {suma_valores(1,2,3,4,5,6,7,8,9)}")