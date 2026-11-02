/*
Ejercicios14.3: Leer 5 elementos numéricos que se introduscan ordenados de forma creciente.
Estos los guadaremos en unatabla de tamaño 10.Leer un números N,
e insertar en el lugar adecuado para la tabla2
continue ordenada.
 */
package ejercicios;

import java.util.Scanner;


public class Ejercicios {
    public static void main(String[] args) {
       
        Scanner entrada = new Scanner(System.in);
        // Creamos un arreglo de tamaño 10 como pide el enunciado
        int[] arreglo = new int[10];
        boolean creciente = true;
        
        System.out.println("Llenar el arreglo:");
        do {
            // Pedimos los 5 elementos ordenados de forma creciente
            for (int i = 0; i < 5; i++) {
                System.out.print((i + 1) + ". Digite un número: ");
                arreglo[i] = entrada.nextInt();
            }
            
            // Verificamos que realmente estén ordenados de forma creciente
            for (int i = 0; i < 4; i++) {
                if (arreglo[i] > arreglo[i+1]) { // Si el actual es mayor al siguiente, no es creciente
                    creciente = false;
                    break;
                } else {
                    creciente = true;
                }
            }
            
            if (!creciente) {
                System.out.println("\nEl arreglo no está ordenado en forma creciente. Digítelos nuevamente.\n");
            }
        } while (!creciente);
        
        System.out.print("\nDigite un número N a insertar: ");
        int numeroN = entrada.nextInt();
        
        // Buscamos en qué posición corresponde insertar el número N
        int sitio_insercion = 0;
        int j = 0;
        
        while (j < 5 && arreglo[j] < numeroN) {
            sitio_insercion++;
            j++;
        }
        
        // Desplazamos los elementos hacia abajo para hacer espacio
        for (int i = 4; i >= sitio_insercion; i--) {
            arreglo[i + 1] = arreglo[i];
        }
        
        // Insertamos el número N en su lugar correspondiente
        arreglo[sitio_insercion] = numeroN;
        
        // Mostramos el arreglo resultante con 6 elementos
        System.out.println("\nEl arreglo queda ordenado de la siguiente manera:");
        for (int i = 0; i < 6; i++) {
            System.out.print(arreglo[i] + " - ");
        }
        System.out.println("");
    }
}

    
    

