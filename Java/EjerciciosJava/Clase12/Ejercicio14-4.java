/*
Leer dos series de 10 enteros, que estaran ordenados crecientemento.
Copiar (fusuinar) las dos tablas en una tercera, de forma que sigan ordenadas
 */
package ejercicios;

import java.util.Scanner;


public class Ejercicio {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int[] arreglo = new int[10];
        int posicion;
        
        System.out.println("Llenar el arreglo de 10 elementos:");
        for (int i = 0; i < 10; i++) {
            System.out.print((i + 1) + ". Digite un número: ");
            arreglo[i] = entrada.nextInt();
        }
        
        // Pedimos la posición a eliminar validando que esté entre 0 y 9
        do {
            System.out.print("\nDigite una posición a eliminar (entre 0 y 9): ");
            posicion = entrada.nextInt();
            if (posicion < 0 || posicion > 9) {
                System.out.println("Posición inválida. Debe estar entre 0 y 9.");
            }
        } while (posicion < 0 || posicion > 9);
        
        // Eliminamos el elemento desplazando los elementos posteriores una posición hacia la izquierda
        for (int i = posicion; i < 9; i++) {
            arreglo[i] = arreglo[i + 1];
        }
        
        // Mostramos el arreglo resultante (ahora con 9 elementos válidos)
        System.out.println("\nEl arreglo resultante sin la posición " + posicion + " es:");
        for (int i = 0; i < 9; i++) {
            System.out.print(arreglo[i] + " - ");
        }
        System.out.println("");
    }
}
