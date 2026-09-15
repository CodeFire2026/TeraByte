# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lisa y que a continuación
# eliminar los elementos repetidos, por último mostrar la lista.

# Creamos una lista
lista = [1,2,3,4,4,5,6,6,7,8,8]

# Creamos una lista vacía para almacenar los elementos sin duplicados
listaSinDuplicados = []

# Recorremos la lista original y agregamos los elementos a la nueva lista solo si no están ya presentes
for i in lista:
    if i not in listaSinDuplicados:
        listaSinDuplicados.append(i)

print(listaSinDuplicados)