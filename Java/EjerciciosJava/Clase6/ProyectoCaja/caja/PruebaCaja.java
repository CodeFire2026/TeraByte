import java.util.Scanner;
import javax.swing.JOptionPane;

public class PruebaCaja {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int ancho, alto, profundidad;

        System.out.println("Como desea ejecutar el programa?");
        System.out.println("1 - Scanner");
        System.out.println("2 - JOptionPane");
        System.out.print("Elija 1 o 2: ");
        int opcion = sc.nextInt();

        if (opcion == 1) {

            System.out.print("Ancho: ");
            ancho = sc.nextInt();

            System.out.print("Alto: ");
            alto = sc.nextInt();

            System.out.print("Profundidad: ");
            profundidad = sc.nextInt();

            Caja caja = new Caja(ancho, alto, profundidad);

            System.out.println("Volumen = " + caja.volumen());

        } else if (opcion == 2) {

            ancho = Integer.parseInt(
                    JOptionPane.showInputDialog("Ingrese el ancho:"));

            alto = Integer.parseInt(
                    JOptionPane.showInputDialog("Ingrese el alto:"));

            profundidad = Integer.parseInt(
                    JOptionPane.showInputDialog("Ingrese la profundidad:"));

            Caja caja = new Caja();
            caja.setAncho(ancho);
            caja.setAlto(alto);
            caja.setProfundidad(profundidad);

            JOptionPane.showMessageDialog(null,
                                          "El vulumen es = " + caja.volumen(),
                                          "Resultado Volumen",
                                          JOptionPane.INFORMATION_MESSAGE);

        } else {
            System.out.println("Opcion invalida.");
        }

        sc.close();
    }
}