
package domain;

public class Persona {

    // Cargamos los atributos
    private int idPersona;
    private static int contadorPersonal;
    private String nombre;
    
    // constructor
    public Persona(String nombre){
        this.nombre = nombre;
        // Incrementar el contador por cada objeto nuevo
        Persona.contadorPersonal++; // No utilizar el operador this
        // Vamos a asignar un nuevo valor a la variable idPersona
        this.idPersona = Persona.contadorPersonal;
    }
    
    public static int getContadorPersonal() {
        return contadorPersonal;
    }

    public static void setContadorPersonal(int aContadorPersonal) {
        contadorPersonal = aContadorPersonal;
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
}
