# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolverá la misma frase pero sin espacios en blanco, y
# además un contador de cuántos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo: frase = vivir por siempre en paz
#           frase final = vivirporsiempreenpaz
#           N° de caracteres = 20


frase = input("Ingrese una frase: ")

sinEspacios = frase.replace(" ", "")

longitud = len(sinEspacios)

print(f"Frase original: {frase}")
print(f"Frase sin espacios: {sinEspacios}")
print(f"N° de caracteres (sin espacios): {longitud}")
