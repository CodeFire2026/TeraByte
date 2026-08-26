package Ejercicio5;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        // Genera un número aleatorio entre 0 y 100
        int numeroAleatorio = (int) (Math.random() * 101);
        int numeroIngresado;
        int intentos = 0;

        do {
            String entrada = JOptionPane.showInputDialog(
                null, 
                "Adivina el número entre 0 y 100:", 
                "Juego de Adivinar", 
                JOptionPane.QUESTION_MESSAGE
            );

            // Control por si el usuario presiona "Cancelar" o cierra la ventana
            if (entrada == null) {
                JOptionPane.showMessageDialog(null, "Juego cancelado.");
                return;
            }

            numeroIngresado = Integer.parseInt(entrada);
            intentos++;

            if (numeroIngresado < numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "Es mayor", "Pista", JOptionPane.INFORMATION_MESSAGE);
            } else if (numeroIngresado > numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "Es menor", "Pista", JOptionPane.INFORMATION_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(
                    null, 
                    "¡Felicidades! Has acertado el número: " + numeroAleatorio + "\nNúmero total de intentos: " + intentos, 
                    "¡Victoria!", 
                    JOptionPane.INFORMATION_MESSAGE
                );
            }
        } while (numeroIngresado != numeroAleatorio);
    }
}