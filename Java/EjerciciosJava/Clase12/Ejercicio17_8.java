/*
Ejercicio 6: Utilizando dos matrices de tamaño 5x9 y 9x5,
cargar la primera y transponerla en la segunda.
*/
package ejercicio17_8;

import java.util.Scanner;

public class Ejercicio17_8 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int matrizA [][] = new int[5][9];
        int matrizB [][] = new int[9][5];

        System.out.println("Ingrese los valores para la matriz de 5x9:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print("Matriz [" + i + "][" + j + "]: ");
                matrizA[i][j] = entrada.nextInt();
            }
        }

        System.out.println("\nMatriz A (5x9):");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(matrizA[i][j] + " ");
            }
            System.out.println();
        }
        
        // Transpongo la matriz A en la matriz B
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                matrizB[j][i] = matrizA[i][j];
            }
        }

        System.out.println("\nMatriz B (9x5) - Transpuesta:");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matrizB[i][j] + " ");
            }
            System.out.println();
        }
    }
}
