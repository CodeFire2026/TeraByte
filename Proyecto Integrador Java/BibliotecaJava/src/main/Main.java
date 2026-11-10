
package main;

import java.util.List;
import java.util.Scanner;
import biblioteca.Biblioteca;
import libro.Libro;

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
                case 3:
                    buscarLibro();
                    break;
                case 4:
                    prestarLibro();
                    break;
                case 5:
                    devolverLibro();
                    break;
                case 6:
                    ordenarLibros();
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

    private static void buscarLibro() {
        System.out.println("\n--- BUSCAR LIBRO ---");

        String texto = leerTexto("Ingrese título o parte del título: ");
        List<Libro> resultados = biblioteca.buscarPorTituloParcial(texto);

        if (resultados.isEmpty()) {
            System.out.println("No se encontraron coincidencias.");
            return;
        }

        System.out.println("Resultados encontrados:");
        for (Libro libro : resultados) {
            System.out.println(libro);
        }
    }

    private static void prestarLibro() {
        System.out.println("\n--- PRESTAR LIBRO ---");

        String titulo = leerTexto("Título: ");
        Libro libro = biblioteca.buscarPorTituloExacto(titulo);

        if (libro == null) {
            System.out.println("Libro no encontrado.");
            return;
        }

        if (biblioteca.prestarLibro(titulo)) {
            System.out.println("Préstamo realizado correctamente.");
        } else {
            System.out.println("No hay stock disponible.");
        }
    }

    private static void devolverLibro() {
        System.out.println("\n--- DEVOLVER LIBRO ---");

        String titulo = leerTexto("Título: ");
        Libro libro = biblioteca.buscarPorTituloExacto(titulo);

        if (libro == null) {
            System.out.println("Libro no encontrado.");
            return;
        }

        if (biblioteca.devolverLibro(titulo)) {
            System.out.println("Libro devuelto correctamente.");
        } else {
            System.out.println("No hay préstamos activos de ese libro.");
        }
    }

    private static void ordenarLibros() {
        if (biblioteca.obtenerLibros().size() <= 1) { // .size() devuelve cauntos elementos hay en la lista
            System.out.println("\nNo hay suficientes libros para ordenar.");
            return;
        }

        biblioteca.ordenarLibros();
        System.out.println("\nLibros ordenados alfabéticamente por título.");
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