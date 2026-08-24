# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1, 3, 2]


lita = [] # Definimos la lista
# Filtramos los elementos menores de 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lita.append(elemento)
print(lita)
