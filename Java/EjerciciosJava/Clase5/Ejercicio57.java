package Ejercicio5.clase5;

import java.util.Scanner;

//Ejercicio 8: Pedir un número N, y mostrar todos los números
//del 1 al N.
public class Ejercicio57 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese un numero para establecer el final del rango a mostrar:");
        int maxNum = entrada.nextInt();
        int i = 1;

        while (i <= maxNum){
            System.out.println(i+" ");
            i++;
        }
        System.out.println();
    }
}
