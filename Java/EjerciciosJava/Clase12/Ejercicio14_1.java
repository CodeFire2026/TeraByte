package Ejercicio5.Clase12;

import java.util.Scanner;
/*I*
Ejercicio 4: Leer 10 números enteros, guardarlos en un
arreglo. Debemos mostrarlos en el siguiente orden: el primero.
        el último, el segundo, el penúltimo, el tercero, etc.
        */
public class Ejercicio14_1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int[] list = new int[10];

        for (int i = 0; i < 10; i++) {

            int number = entrada.nextInt();

            list[i]=number;

        }

        int contador = 9;

        System.out.print("[");
        for (int i = 0; i < 5; i++) {
            if(i != 0){
                System.out.print(",");
            }

            System.out.print(list[i] + "," + list[contador]);
            contador--;

        }
        System.out.print("]");
    }

}
