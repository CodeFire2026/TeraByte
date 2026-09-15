#Ejercicio 5: Factorial de un número positivo
#Hacer un programa para calcular el factorial de un número positivo

def factorial(numero):
    if numero < 0:
        return "El numero debe ser +"
    elif numero == 0:
        return 1
    else:
        resultado = 1
        while numero > 1:
            resultado *=numero
            numero -=1
        return resultado

print(factorial(3))
print(factorial(4))
print(factorial(-1))
print(factorial(0))