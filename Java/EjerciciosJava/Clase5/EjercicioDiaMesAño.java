
package Operaciones;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class EjercicioDiaMesAño {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int opcion;
        int dia;
        int mes;
        int año;
        int continuar = 1;

        while (continuar == 1) {

            System.out.println("\n===== MENU =====");
            System.out.println("1. Validar fecha con Scanner");
            System.out.println("2. Validar fecha con JOptionPane");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opcion: ");

            opcion = entrada.nextInt();

            switch (opcion) {

                case 1:

                    System.out.print("Ingrese el dia: ");
                    dia = entrada.nextInt();

                    System.out.print("Ingrese el mes: ");
                    mes = entrada.nextInt();

                    System.out.print("Ingrese el anio: ");
                    año = entrada.nextInt();

                    if (dia >= 1 && dia <= 30 &&
                        mes >= 1 && mes <= 12 &&
                        año > 0) {

                        System.out.println("La fecha es correcta.");

                    } else {

                        System.out.println("La fecha es incorrecta.");
                    }

                    break;

                case 2:

                    dia = Integer.parseInt(
                            JOptionPane.showInputDialog("Ingrese el dia:")
                    );

                    mes = Integer.parseInt(
                            JOptionPane.showInputDialog("Ingrese el mes:")
                    );

                    año = Integer.parseInt(
                            JOptionPane.showInputDialog("Ingrese el anio:")
                    );

                    if (dia >= 1 && dia <= 30 &&
                        mes >= 1 && mes <= 12 &&
                        año > 0) {

                        JOptionPane.showMessageDialog(
                                null,
                                "La fecha es correcta."
                        );

                    } else {

                        JOptionPane.showMessageDialog(
                                null,
                                "La fecha es incorrecta."
                        );
                    }

                    break;

                case 3:

                    continuar = 0;
                    System.out.println("Programa finalizado.");

                    break;

                default:

                    System.out.println("Opcion incorrecta.");
            }

            if (continuar == 1) {

                System.out.println("\n¿Desea continuar?");
                System.out.println("1. Si");
                System.out.println("2. No");
                System.out.print("Seleccione una opcion: ");

                continuar = entrada.nextInt();
            }
        }
    }
}
