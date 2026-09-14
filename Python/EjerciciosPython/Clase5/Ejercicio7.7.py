# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viseversa.
# Investigar las formulas

def celsius_to_fahrenheit():
    c = float(input("Dato entero de gracos C° para pasar F°\n"))
    return str(((c*(9/5)) + 32)) + " F°"


def fahrenheit_to_celsius():
   f = float(input("Dato entero de gracos F° para pasar C°\n"))
   return str(((f-32) * 5/9)) + " C°"


def select_menu():
    while True:
        s = input("Bienvenido al programa para pasar de C° a F° o viceversa\n"
    "Ingrese el numero de la accion que quiere hacer\n"
    "1 - C° -> F°\n"
    "2 - F° -> C°\n"
    "Cualquier numero - salir\n")
        if(s == "1"):
            print(celsius_to_fahrenheit())
        elif(s == "2"):
            print(fahrenheit_to_celsius())
        else:
            break
    return "Que tenga buen dia"
    

print(select_menu())