/*
Pedir números hasta que se introduzca uno negativo y mostrar cuántos números se han introducido.
utilizando Scanner
 */
package TareaClase3;

import java.util.Scanner;

public class Ejercicio4Scanner {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int numero;
        int cantidad = 0;

        System.out.print("Ingrese un número: ");
        numero = entrada.nextInt();

        while (numero >= 0) {
            cantidad++;
            System.out.print("Ingrese otro número: ");
            numero = entrada.nextInt();
        }

        System.out.println("Se introdujeron " + cantidad + " números.");
        System.out.println("El programa a finalizado por numero negativo");
    }
}
