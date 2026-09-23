package Ejercicio5.Clase7;

import javax.swing.*;
import java.util.Scanner;
/*
Ejercicio 11: Diseñar un programa que muestre el producto
de los 10 primeros números impares
Hacerlo con JOptionPane I
*/

public class Ejercicio72 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int opcion;
        int continuar = 1;
        while (continuar == 1) {

            System.out.println("\n===== MENU =====");
            System.out.println("1. Mostrar el producto de los primeros 10 numeros impares con Scanner");
            System.out.println("2. Mostrar el producto de los primeros 10 numeros impares con JOptionPane");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opcion: ");

            opcion = entrada.nextInt();

            long producto = 1;

            for (int i = 0; i < 10; i++) {
                producto *= (2 * i + 1);
            }

            switch (opcion) {

                case 1:
                    System.out.println("El producto de los 10 primeros números impares es: " + producto);
                    break;

                case 2:
                    JOptionPane.showMessageDialog(null,
                                                  "El producto de los 10 primeros números impares es:\n" + producto,
                                                  "Resultado", JOptionPane.INFORMATION_MESSAGE);
                    System.exit(0);
                    break;

                case 3:
                    continuar = 0;
                    System.out.println("Programa finalizado.");
                    break;

                default:
                    System.out.println("Opción incorrecta.");
            }

            if (continuar == 1) {
                System.out.println("\n¿Desea continuar?");
                System.out.println("1. Sí");
                System.out.println("2. No");
                System.out.print("Seleccione una opción: ");

                continuar = entrada.nextInt();
            }
        }
    }
}
