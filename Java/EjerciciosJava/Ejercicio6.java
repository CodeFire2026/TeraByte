package Ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            int numero;
            int suma = 0;
            
            do {
                System.out.print("Digite un número (0 Para salir): ");
                numero = Integer.parseInt(entrada.nextLine());
                
                suma += numero; // Acumulamos la suma
                
            } while (numero != 0); // El ciclo se repite mientras el número no sea 0
            
            System.out.println("La suma de todos los números ingresados es: " + suma);
        }
    }
}