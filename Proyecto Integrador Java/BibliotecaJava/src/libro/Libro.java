
package libro;

public class Libro {
    private final String titulo; //Atributos
    private final String autor;
    private int stock;
    private int prestados;

    //Constructor
    public Libro(String titulo, String autor, int stock) { // Parametros
        this.titulo = titulo;
        this.autor = autor;
        this.stock = stock;
        this.prestados = 0;
    }

    public String getTitulo() { // Consulta los datos
        return this.titulo;
    }

    public String getAutor() {
        return this.autor;
    }

    public int getStock() {
        return this.stock;
    }

    public int getPrestados() {
        return this.prestados;
    }
    
    //Metodo
    public boolean prestar() {
        if (stock > 0) {
            stock--;
            prestados++;
            return true;
        }
        return false;
    }
    
    
    public boolean devolver() {
        if (prestados > 0) {
            prestados--;
            stock++;
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return "Titulo: " + titulo + " - " + "Autor: "+ autor
                + " | Stock: " + stock
                + " | Prestados: " + prestados;
    }
}

