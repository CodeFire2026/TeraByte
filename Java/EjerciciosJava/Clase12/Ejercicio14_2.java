package Ejercicio5.Clase12;

/*
Ejercicio 5: Leer por teclado dos tablas de 10 números
enteros y mezclarlas en una tercera de la forma: el 1ª de
A, el 1ª de B, el 2a de A, el 2ª de B, etc.

*/

import java.util.Scanner;

public class Ejercicio14_2 {

    public static void main(String[] args){

        Scanner entrada = new Scanner(System.in);

        int[] list1= new int[10];
        int[] list2 = new int[10];

        for (int i = 0; i < 10; i++) {

            int number = entrada.nextInt();

            list1[i]=number;

        }

        for (int i = 0; i < 10; i++) {

            int number = entrada.nextInt();

            list2[i]=number;

        }

        int[] finalList = new int[20];

        int index = 0;

        for (int i = 0; i < list1.length; i++) {

            finalList[index] = list1[i];

            finalList[index+1] = list2[i];

            index+=2;

        }

        System.out.print("[");
        for(int i = 0; i < finalList.length; i++) {

            System.out.print(finalList[i]);
            if(finalList.length-1 > i){
                System.out.print(",");
            }


        }
        System.out.print("]");

    }

}
