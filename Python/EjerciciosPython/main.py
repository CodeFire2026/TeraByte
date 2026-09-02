seleccionArgentina = {
    23: {"Nombre": "Emiliano Martínez", "Edad": 34, "Altura": 1.95, "Precio": "17.4 Millones", "Posición": "Portero"},
    9: {"Nombre": "Lautaro Martínez", "Edad": 29, "Altura": 1.74, "Precio": "99 Millones", "Posición": "Delantero Centro"},
    19: {"Nombre": "Julián Álvarez", "Edad": 26, "Altura": 1.70, "Precio": "104.8 Millones", "Posición": "Delantero"},
    5: {"Nombre": "Enzo Fernández", "Edad": 25, "Altura": 1.78, "Precio": "104.8 Millones", "Posición": "Mediocampista"},
    20: {"Nombre": "Alexis Mac Allister", "Edad": 27, "Altura": 1.76, "Precio": "93.1 Millones", "Posición": "Mediocampista"},
    13: {"Nombre": "Cristian Romero", "Edad": 28, "Altura": 1.85, "Precio": "58.2 Millones", "Posición": "Defensa Central"},
    6: {"Nombre": "Lisandro Martínez", "Edad": 28, "Altura": 1.75, "Precio": "46.5 Millones", "Posición": "Defensa Central"},
    16: {"Nombre": "Nico Paz", "Edad": 21, "Altura": 1.85, "Precio": "75.7 Millones", "Posición": "Mediocampista"},
    22: {"Nombre": "Giuliano Simeone", "Edad": 23, "Altura": 1.80, "Precio": "46.5 Millones", "Posición": "Delantero"},
    3: {"Nombre": "Valentín Barco", "Edad": 22, "Altura": 1.72, "Precio": "40.7 Millones", "Posición": "Lateral Izquierdo"}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end=" ")
print(len(seleccionArgentina))
