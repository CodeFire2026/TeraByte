package Ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        // Genera un número aleatorio entre 0 y 100
        int numeroAleatorio = (int) (Math.random() * 101);
        int numeroIngresado;
        int intentos = 0;

        System.out.println("=== ¡Juego de Adivinar el Número! ===");
        
        do {
            System.out.print("Introduce un número (0-100): ");
            numeroIngresado = entrada.nextInt();
            intentos++;

            if (numeroIngresado < numeroAleatorio) {
                System.out.println("Es mayor");
            } else if (numeroIngresado > numeroAleatorio) {
                System.out.println("Es menor");
            } else {
                System.out.println("\n¡Felicidades! Has acertado el número: " + numeroAleatorio);
                System.out.println("Número total de intentos: " + intentos);
            }
        } while (numeroIngresado != numeroAleatorio);

        entrada.close();
    }
}