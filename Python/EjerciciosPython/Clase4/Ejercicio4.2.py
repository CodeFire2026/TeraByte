# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repeticiones)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

lista1 = ["Pyhton", "Java", "JavaScript", "Hola", "Mundo"]
lista2 = ["Pyhton", "Java", "JavaScript", "Go"]

# Convertimos las listas a conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Palabras que aparecen en las listas (sin repeticiones)
listaTotal = list(conjunto1 | conjunto2)

# Palabras que aparecen en la primera lista pero no en la segunda
soloLista1 = list(conjunto1 - conjunto2)

# Palabras que aparecen en la segunda lista
soloLista2 = list(conjunto2 - conjunto1)

# Palabras que aparecen en ambas listas
ambasListas = list(conjunto1 & conjunto2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)

print("\n1. Palabras que aparecen en las listas:")
print(listaTotal)

print("\n2. Palabras solo de la primera lista:")
print(soloLista1)

print("\n3. Palabras solo de la segunda lista:")
print(soloLista2)

print("\n4. Palabras que aparecen en ambas listas:")
print(ambasListas)
