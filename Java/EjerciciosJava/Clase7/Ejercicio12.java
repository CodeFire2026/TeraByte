import java.util.Scanner;

public class Ejercicio12 {
    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            System.out.print("Digite un número para calcular su factorial: ");
            int numero = entrada.nextInt();
            
            long factorial = 1;
            for (int i = 1; i <= numero; i++) {
                factorial *= i; // Multiplica acumulativamente
            }
            
            System.out.println("El factorial de " + numero + " es: " + factorial);
        }
    }
}

    

