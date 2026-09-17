/*
Ejercicio 6.8: Pedir 10 números y escribir la suma total
Hacerlo con la clase Scanner y JOptionPane
*/
package Ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class EJercicio68 {
   public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int opcion;
        int continuar = 1;

        while (continuar == 1) {

            System.out.println("\n===== MENU =====");
            System.out.println("1. Sumar 10 números con Scanner");
            System.out.println("2. Sumar 10 números con JOptionPane");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opcion: ");

            opcion = entrada.nextInt();

            switch (opcion) {

                case 1:
                    int sumaScanner = 0;
                    int numeroScanner;

                    System.out.println("\nIngrese 10 números:");
                    for (int i = 1; i <= 10; i++) {
                        System.out.print("Número " + i + ": ");
                        numeroScanner = entrada.nextInt();
                        sumaScanner += numeroScanner;
                    }

                    System.out.println("La suma total es: " + sumaScanner);
                    break;

                case 2:
                    int sumaJOption = 0;
                    int numeroJOption;

                    for (int i = 1; i <= 10; i++) {
                        numeroJOption = Integer.parseInt(
                                JOptionPane.showInputDialog("Ingrese el número " + i + ":")
                        );
                        sumaJOption += numeroJOption;
                    }

                    JOptionPane.showMessageDialog(
                            null,
                            "La suma total es: " + sumaJOption
                    );
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
