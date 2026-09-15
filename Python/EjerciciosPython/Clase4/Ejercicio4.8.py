#Ejercicio 3: Insertar elementos y ordenarlos
#Pedir números y meterlos en una lista, cuando el usuario
#Introduzca un número 0, nuestro programa dejaría de insertar.
#Por último, mostrar los números ordenados de menor a mayor.

numeros =[3,7,12]
print(numeros)
valorNum= int(input("Introduce un numero: "))

while valorNum != 0:
    numeros.append(valorNum)
    print(numeros)
    valorNum= int(input('Ingresar otro número: '))

numeros.sort()
print(nueros)