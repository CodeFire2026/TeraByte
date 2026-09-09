import math # Importamos la clase math para hacer uso de la función sqrt(raiz cuadrada)

# Ejercicio de matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo: "))
while (numero < 0):
    print("Error -> deveria ser un numero positivo")
    numero = int(input("Digite un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero):.2f}")