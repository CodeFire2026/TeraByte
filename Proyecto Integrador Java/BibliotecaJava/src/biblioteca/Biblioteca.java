
package biblioteca;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import libro.Libro;

public class Biblioteca {
    private final List<Libro> libros; //Atributo

    //Constructor
    public Biblioteca() {
        libros = new ArrayList<>(); // crea una lista vacía para guardar los libros.
    }

    //Metodo
    public Libro buscarPorTituloExacto(String titulo) { // Parametro
        for (Libro libro : libros) { // Se recorre cada libro dentro de la lista libros de la biblioteca.  
            if (libro.getTitulo().equalsIgnoreCase(titulo)) { // es un metodo que que compara dos textos ignorando mayúsculas y minúsculas
                return libro;
            }
        }
        return null;
    }
    
    public List<Libro> buscarPorTituloParcial(String texto) {
        List<Libro> resultados = new ArrayList<>();

        for (Libro libro : libros) {
            if (libro.getTitulo().toLowerCase().contains(texto.toLowerCase())) { // .contains verifica si el título contiene la cadena buscada
                resultados.add(libro);
            }
        }

        return resultados;
    }
    
    public boolean agregarLibro(String titulo, String autor, int stock) {
        if (buscarPorTituloExacto(titulo) != null) {
            return false;
        }

        libros.add(new Libro(titulo, autor, stock));
        return true;
    }

    public boolean estaVacia() {
        return libros.isEmpty(); // .isEmpty() es un metodo que devuelve un boolena si contiene algo o no
    }

    public List<Libro> obtenerLibros() {
        return libros;
        public boolean prestarLibro(String titulo) {
        Libro libro = buscarPorTituloExacto(titulo);

        if (libro == null) {
            return false;
        }

        return libro.prestar();
    }

    public boolean devolverLibro(String titulo) {
        Libro libro = buscarPorTituloExacto(titulo);

        if (libro == null) {
            return false;
        }

        return libro.devolver();
    }

    public void ordenarLibros() {
        libros.sort(Comparator.comparing( // .sort Este método recibe un comparador que define cómo se deben ordenar los elementos
                Libro::getTitulo, String.CASE_INSENSITIVE_ORDER // String.CASE_INSENSITIVE_ORDER es un comparador especial de Java que compara cadenas ignorando mayúsculas/minúsculas
        )); // Libro::getTitulo es una referencia a método, usa el título del libro como clave para comparar
    }

    
}

