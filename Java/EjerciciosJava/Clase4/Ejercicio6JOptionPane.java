
package Ejercicio6;

import javax.swing.JOptionPane;
 
        public class Ejercicio6JOptionPane {
    public static void main(String[] args) {
        int numero;
        int suma = 0;

        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número (0 para salir):"));
            
            suma += numero;

        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "La suma de todos los números ingresados es: " + suma);
        
    }
    
        }

    

