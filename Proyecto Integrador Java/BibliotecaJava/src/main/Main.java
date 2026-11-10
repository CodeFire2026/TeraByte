
package main;

import biblioteca.Biblioteca;
import libro.Libro;

import java.util.List;
import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);
    private static final Biblioteca biblioteca = new Biblioteca();

    public static void main(String[] args) {
        int opcion;

        do {
            mostrarMenu();
            opcion = leerEntero("Seleccione una opción: ");

            switch (opcion) {
                case 1:
                    agregarLibro();
                    break;
                case 2:
                    mostrarLibros();
                    break;
                case 7:
                    System.out.println("\nPrograma finalizado. ¡Hasta luego!");
                    break;
                default:
                    System.out.println("\nOpción inválida. Intente nuevamente.");
            }
        } while (opcion != 7);

    }

    private static void mostrarMenu() {
        System.out.println("\n=================================");
        System.out.println("        SISTEMA BIBLIOTECA");
        System.out.println("=================================");
        System.out.println("1. Agregar libro");
        System.out.println("2. Mostrar libros");
        System.out.println("3. Buscar libro");
        System.out.println("4. Prestar libro");
        System.out.println("5. Devolver libro");
        System.out.println("6. Ordenar libros");
        System.out.println("7. Salir");
        System.out.println("=================================");
    }

    private static void agregarLibro() {
        System.out.println("\n--- AGREGAR LIBRO ---");

        String titulo = leerTexto("Título: ");

        if (biblioteca.buscarPorTituloExacto(titulo) != null) {
            System.out.println("El libro ya existe.");
            return;
        }

        String autor = leerTexto("Autor: ");
        int stock = leerEnteroNoNegativo("Stock: ");

        if (biblioteca.agregarLibro(titulo, autor, stock)) {
            System.out.println("Libro agregado correctamente.");
        }
    }

    private static void mostrarLibros() {
        System.out.println("\n--- LISTADO DE LIBROS ---");

        if (biblioteca.estaVacia()) {
            System.out.println("No hay libros cargados.");
            return;
        }

        for (Libro libro : biblioteca.obtenerLibros()) {
            System.out.println(libro);
        }
    }

    private static String leerTexto(String mensaje) {
        while (true) {
            System.out.print(mensaje);
            String texto = scanner.nextLine().trim();

            if (!texto.isEmpty()) {
                return texto;
            }

            System.out.println("El dato no puede estar vacío.");
        }
    }

    private static int leerEntero(String mensaje) {
        while (true) {
            System.out.print(mensaje);
            String entrada = scanner.nextLine().trim();

            try {
                return Integer.parseInt(entrada);
            } catch (NumberFormatException e) {
                System.out.println("Ingrese un número entero válido.");
            }
        }
    }

    private static int leerEnteroNoNegativo(String mensaje) {
        while (true) {
            int valor = leerEntero(mensaje);

            if (valor >= 0) {
                return valor;
            }

            System.out.println("El valor no puede ser negativo.");
        }
    }
}

