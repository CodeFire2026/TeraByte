
import javax.swing.JOptionPane;

public class Ejercicio_12 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número para calcular su factorial:"));
        
        long factorial = 1;
        for (int i = 1; i <= numero; i++) {
            factorial *= i; // Multiplica acumulativamente
        }
        
        JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
    }
}