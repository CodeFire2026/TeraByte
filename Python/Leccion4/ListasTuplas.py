# Lista = Claudio, German, Veronica, Gema
# Coecciones en Python

# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

nombres = ["Claudio", "German", "Veronica", "Gema"]
""""
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-3])
print(nombres[-2])
"""

print(nombres)
print(nombres[0:2]) #Solo muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista alindice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0, 1, 2
#desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor 
nombres[2] = "Marcelo"
nombres[0] = "Sebastian"
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene 
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento

nombres.append('Juan')
nombres.append([1, 2, 3])
nombres.append([True])
nombres.append([10.45])
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# Insertar un elemento e un indice especifico

nombres.insert(1,'Lidia')
print(nombres)
nombres.insert(3, 'Micaela')
print(nombres)

# Eliminamos un elemento
nombres.remove('Micaela')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2] # Del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) #Aqui nos muestra error

#Definimos una tupla
cocina = ('cuchara', 'cuchillo','tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchets no parentesis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un  rango
print(cocina[0:2])
# Ejemplo 
verduras = ('papa',) #una tupla necesita aunque sea de un elemento la coma
# De lo contrario solo seria un tipo str cadena

# Recorrcomos los elementos de la tupla
for cocinar in cocina: # Print esta usando \n para saltos de lineas
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de linaes

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina es para eliminar la tupla

# Tipo set 

planetas = {'marte', 'Jupiter', 'Venus'}
print(len(planetas)) # Usamos la funcion len = length significa largo

#Revisar si un elemento existe dentro de set
print('Jupiter' in planetas)

# Agregar un elemento 
planetas.add('Tierra') # add es una funcion
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter')
print(planetas)
planetas.discard('Tierra') # Esta funcion no nos precenta ningun error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
#print(planetas) # Al eliminar nos muestra fun error

# 'Maradona' :10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# DICT(KEY,VALUE)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos' ,
    'SABD':'Sistema de Administracion de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar otro elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muesta solo las llaves

for valor in diccionario.values(): # Usamos una funcion para aceeder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # el diccionario se borro


# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
# Print(lista3.index(0)) # ESto daria un error por no ser un elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuaneta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamineto, en python es una funcion
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena Descendentemente
print(lista3)

tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener difenrentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

