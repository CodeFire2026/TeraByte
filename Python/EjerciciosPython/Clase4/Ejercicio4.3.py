#Ejercicio 3: Agregar personajes a una lista

# Escriba un programa donde cree una Lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [
    {"Nombre": "Aragorn","Clase": "Guerrero","Raza": "Dúnadan del norte"},
    {"Nombre": "Gandalf","Clase": "Mago","Raza": "Istar"},
    {"Nombre": "Legolas","Clase": "Arquero","Raza": "Elfo Sindar"},
    {"Nombre": "Frodo","Clase": "Portador del Anillo","Raza": "Hobbit"},
    {"Nombre": "Gimli","Clase": "Guerrero","Raza": "Enano"}
]

# Mostramos los personajes
for personaje in personajes:
    print(f"Nombre: {personaje['Nombre']}, Clase: {personaje['Clase']}, Raza: {personaje['Raza']}")







