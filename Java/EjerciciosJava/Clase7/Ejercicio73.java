// Ejercicio 12: Pedir un número y calcular su factorial
// Hacerlo con las dos clases, Scanner y JOptionPane.

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio73 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int opcion;
        int continuar = 1;
        while (continuar == 1) {
            System.out.println("\n===== MENU =====");
            System.out.println("1. Calcular factorial con Scanner");
            System.out.println("2. Calcular factorial con JOptionPane");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opcion: ");
            opcion = entrada.nextInt();
            switch (opcion) {
                case 1:
                    System.out.print("Ingrese un número: ");
                    int numero = entrada.nextInt();
                    long factorial = 1;
                    for (int i = 1; i <= numero; i++) {
                        factorial = factorial * i;
                    }
                    System.out.println("El factorial de " + numero + " es: " + factorial);
                    break;
                case 2:
                    int numeroJOption = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número:"));
                    long factorialJOption = 1;
                    for (int i = 1; i <= numeroJOption; i++) {
                        factorialJOption = factorialJOption * i;
                    }
                    JOptionPane.showMessageDialog(null, "El factorial de " + numeroJOption + " es: " + factorialJOption,
                            "Resultado", JOptionPane.INFORMATION_MESSAGE);
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
        entrada.close();
    }
}
