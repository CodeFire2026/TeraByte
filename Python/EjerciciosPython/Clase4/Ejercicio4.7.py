#Ejercicio 2: Modificar los elementos de una lista
#Llenar una lista con los números del 1 al 10, luego modificar
#los elementos de la lista multiplicándolos por un valor ingresado por el usuario

#Llenar la lista
numeros = [1,2,3,4,5,6,7,8,9,11]

print(numeros)
numeros[9] = 10
print(numeros)

#Multiplicando por un valor que ingresa el usuario
multiplicador = int(input("Ingrese un numero: "))
for i in range(len(numeros)):
    numeros[i] = numeros[i] * multiplicador

print(numeros)
