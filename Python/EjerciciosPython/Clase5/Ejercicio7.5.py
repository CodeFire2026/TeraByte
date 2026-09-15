#Ejercicio 3: Función Recursiva
#Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# puede ser cualquier valor positivo, por ejemplo, si pasamos el valor
# de 5, debe imprimir;
#5
#4
#3
#2
#1
#En caso de ser el número 3 debe imprimir:
#3
#2
#1
#Si se ingresan números negativos no imprime nada

def num_decendentes(n):
    if n < 1:
        return
    else:
        print(n)
        num_decendentes(n - 1 )
print('Imprimir desde 5:')
num_decendentes(5)

print('Imprimir desde 3:')
num_decendentes(3)

print('No imprime números negativos')
num_decendentes(-5)


