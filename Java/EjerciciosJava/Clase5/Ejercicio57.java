package Ejercicio5.Clase5;

import javax.swing.*;
import java.util.Scanner;

//Ejercicio 8: Pedir un número N, y mostrar todos los números
//del 1 al N.
public class Ejercicio57 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("1 - Terminal");
        System.out.println("2 - JOptionPane");

        int opcion = entrada.nextInt();

        switch (opcion){
            case 1:terminal(entrada);
            break;
            case 2:modeJOptionPane();
            break;
            default:
                System.out.println("Opcion invalida");
        }
    }
    private static void terminal(Scanner entrada){
        System.out.println("Ingrese un numero para establecer el final del rango a mostrar: ");
        int maxNum = entrada.nextInt();

        for (int i = 1; i <= maxNum; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        System.out.println("Desea Repetir");
        System.out.println("1 - Si");
        System.out.println("2 - No");
        int repetir =entrada.nextInt();

        if(repetir == 1) {
            terminal(entrada);
        }
    }
    private static void modeJOptionPane(){
        String texto = JOptionPane.showInputDialog("Ingrese un numero para establecer el final del rango a mostrar: ");

        if(texto == null){
            JOptionPane.showMessageDialog(null,"Ingrese un valor");
            return;
        }

        int maxNum = Integer.parseInt(texto.trim());

        StringBuilder sb = new StringBuilder();

        for (int i = 1; i <= maxNum; i++) {
            sb.append(i).append(" ");
        }

        JOptionPane.showMessageDialog(null,
                                      "Numeros del 1 al " + maxNum + ":\n" + sb);

        int  repetir = JOptionPane.showConfirmDialog(null,
                                                     "Desea repetir", "Repetir",
                                                     JOptionPane.YES_NO_OPTION);
        if(repetir == JOptionPane.YES_OPTION){
            modeJOptionPane();
        }
    }

}
