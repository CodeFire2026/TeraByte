/*
Ejercicio 15: Leer 10 enteros ordenados crecientemente. Leer N y buscarlo en la
tabla. Se debe mostrar la posición en que se encuentra. Si no está, indicarlo
con un mensaje.
*/
package ejercicio14_7;

import java.util.Scanner;

public class Ejercicio14_7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numeros [] = new int[10];
        int N;
        boolean encontrado = false;

        System.out.println("Ingrese 10 enteros ordenados crecientemente:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = entrada.nextInt();
        }

        System.out.print("\nIngrese el número a buscar: ");
        N = entrada.nextInt();

        // Buscar el numero ingresado en el arreglo
        for (int i = 0; i < 10; i++) {
            if (numeros[i] == N) {
                System.out.println("El número " + N + " se encuentra en la posición: " + i);
                encontrado = true;
                break;
            }
        }
        if (encontrado == false) {
            System.out.println("El número " + N + " no está en la tabla.");
        }
    }
}
