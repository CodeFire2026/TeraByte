# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.

import random

# Número aleatorio entre 1 y 100
numeroRandom = random.randint(1, 100)

# Contador de intentos
intentos = 0

# Pedimos números hasta que el usuario acierta
while True:
    usuarioNum = int(input("Ingrese un número: "))
    intentos += 1
    if usuarioNum < numeroRandom:
        print("Es mayor")
    elif usuarioNum > numeroRandom:
        print("Es menor")
    else:
        print(f"¡Es correcto! Número acertado: {numeroRandom} ")
        print(f"Número de intentos: {intentos}")
        break

