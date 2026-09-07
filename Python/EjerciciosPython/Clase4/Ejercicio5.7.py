# Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo inicial de 1000$ y tendrá el siguiente menú de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir


# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 0;

while True:
    print("Bienvenido al cajero automatico")
    print("Su saldo es:", saldo)
    print("Seleccione una opción:")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    accion = input("Opcion:")

    if accion == "1":
        ingreso = float(input("Ingrese el monto a depositar: "))
        if ingreso > 0: 
            saldo += ingreso
            print("Se ha ingresado:", ingreso)
        else:
            print("Monto invalido")
    elif accion == "2":
        retiro = float(input("Ingrese el monto a retirar: "))

        if retiro > 0: 
            saldo -= retiro
            print("Se ha retirado:", retiro)
        else:
            print("Monto invalido")

    elif accion == "3":
        print("Su saldo disponible es:", saldo)
    elif accion == "4":
        print("Gracias por usar el cajero automatico")
        break

