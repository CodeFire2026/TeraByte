# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizándolo argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumento

def multiplicar_valores(*args: int):
    resultado = 1

    for numero in args:
        resultado *= numero

    return resultado

print(f"La multiplicación de los argumentos es: {multiplicar_valores(1,2,3,4,5)}")