
package test;

import domain.Empleado;
import domain.Cliente;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Mauro", 57000.0);
        System.out.println("empleado1 = " + empleado1);
        
        Cliente cliente1 = new Cliente(new Date(), true, "Carlos", 'M', 40, "Ballofet 5400");
        System.out.println("cliente1 = " + cliente1);
    }
}
