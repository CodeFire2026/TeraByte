# Importamos la clase math para hacer uso de la función sqr(ra+iz cuadrada)
import math
# Ejercicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo
numero = int(input("Ingrese un número positivo: "))
while numero < 0:
    print("Error -> Debería ser un número positivo")
    numero = int(input("Ingrese un número positivo: "))
print(f"\nSu raíz cuadrada es: {math.sqrt(numero):.2f}")