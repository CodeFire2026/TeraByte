# Ejercicio 1: llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar
# la lista con el bucle for, los elementos deben mostrarse
# de la siguiente forma:
# 1-2-3-4-5...-50

numeros = list(range(1, 51))

# Mostrar los elementos separados por guiones
for i in range(len(numeros)):
    if i < len(numeros) - 1:
        print(numeros[i], end="-")
    else:
        print(numeros[i])
