/*
Pedir números hasta que se introduzca uno negativo y mostrar cuántos números se han introducido.
utilizando JOptionPane.
 */
package TareaClase3;

import javax.swing.JOptionPane;

public class Ejercicio4JOptionPane {
    public static void main(String[] args) {

        int numero;
        int cantidad = 0;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número:"));

        while (numero >= 0) {
            cantidad++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número:"));
        }

        JOptionPane.showMessageDialog(null,"Se introdujeron " + cantidad + " números.");
        JOptionPane.showMessageDialog(null,"El programa a finalizado por numero negativo");
    }
}
