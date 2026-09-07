#Ejercicio 4: Sumar numeros pares dentro de un rango
# Hacer un programa para sumar números pares dentro # de un rango, por ejemplo:
#
# suma de números pares del 2 al 30 suma = 240

def sumPares(inicioRango,finalRango):
    suma = 0
    iterator = inicioRango
    while iterator <= finalRango:
        if iterator % 2 == 0:
            suma += iterator
        iterator += 1
    return suma


print(sumPares(1, 30));
print(sumPares(1, 100));