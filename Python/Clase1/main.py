# Lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres [0])
print(nombres [-1])
print(nombres [0:2]) # Solo muestra el índice 0 y 1 pero no el índice 2
# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres [ :3]) # Indices a mistrar 0, 1, 2
# Desde el índice indicado hasta el final
print(nombres [1: ])
# Modificamos un valor
nombres[2] = "Liliana"
print(nombres)
nombres[0] = "Natalia"
print(nombres)

# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) # Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Marcelo")
print(nombres)

# Inserta un elemento en un índice específico
nombres.insert(1, "Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un índice específico
del nombres[2] # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
# del nombres
# print(nombres) # Aquí nos dara un error


# Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no paréntesis
print(cocina[0])

# Mostrar de la manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])
# Ejemplo
verduras = ("papa",) # Una tupla necesita aunque sea de un elemento: la como
# De lo contrario solo serai de tipo str cadena

# Recorremos los elmentos de la tupla
for cocinar in cocina: # Print está usando \n para saltos de líneas
    print(cocinar, end=" ") # Usamos end para eliminar los saltos de líneas

# Convercion de tupla lista y de lista a tupla para modificarla
cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

# del cocina (para eliminar la tupla)


