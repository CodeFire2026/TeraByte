
/*import java.util.Scanner;*/
import javax.swing.JOptionPane;

/*Ejercicio 3: Leer números hasta que se introduzca un cero
Para cada uno indicar si es par o impar
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane */
public class Ejercicio1 {

    public static void main(String[] args) {
        /*Ejercicio hecho con Scanner*/
        
        /*Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Ingrese un número (0 para terminar):");
        numero = entrada.nextInt();
        while (numero != 0) {
            if (numero % 2 == 0) {
                System.out.println("El número " + numero + " es par.");
            } else {
                System.out.println("El número " + numero + " es impar.");
            }
            System.out.println("Ingrese otro número (0 para terminar):");
            numero = entrada.nextInt();
        }
        System.out.println("Programa finalizado.");*/

        /*Ejercicio hecho con JOptionPane*/
        int numero;
        numero = Integer.parseInt(
                JOptionPane.showInputDialog("Ingrese un número (0 para terminar):")
        );
        while (numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null,
                        "El número " + numero + " es par."
                );
            } else {
                JOptionPane.showMessageDialog(null,
                        "El número " + numero + " es impar."
                );
            }
            numero = Integer.parseInt(
                    JOptionPane.showInputDialog("Ingrese otro número (0 para terminar):")
            );
        }
        JOptionPane.showMessageDialog(
                null,
                "Programa finalizado."
        );
    }
}
