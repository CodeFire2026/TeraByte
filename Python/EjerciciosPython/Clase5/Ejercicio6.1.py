# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres

palabra = input("Ingrese una palabra: ")

lista = []

for caracteres in palabra:
    if caracteres not in lista:
        lista.append(caracteres)

print("Lista sin caracteres repetidos:", lista)