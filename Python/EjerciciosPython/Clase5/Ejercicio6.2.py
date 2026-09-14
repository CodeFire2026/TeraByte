# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el teléfono, el programa tendrá el siguiente menú de opciones:
#     1. Nuevo contacto
#     2. Borrar contacto
#     3. Ver contactos existentes
#     4. Salir

# Ejercicio 11: Agenda telefonica

def mostrar_menu():
    print("\n--- Agenda Telefónica ---")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")

def agenda():
    contactos = {}
    opcion = ""  # inicializamos la variable
    while opcion != "4":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono: ")
            contactos[nombre] = telefono
            print(f"Contacto {nombre} agregado.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a borrar: ")
            if nombre in contactos:
                del contactos[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print("El contacto no existe.")

        elif opcion == "3":
            if contactos:
                print("\n--- Contactos ---")
                for nombre, telefono in contactos.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("No hay contactos guardados.")

        elif opcion == "4":
            print("Saliendo de la agenda...")

        else:
            print("Opción inválida. Intente nuevamente.")

agenda()
