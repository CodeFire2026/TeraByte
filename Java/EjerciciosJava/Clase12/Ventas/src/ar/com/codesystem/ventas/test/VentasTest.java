
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Remera", 5500.00);
        Producto producto4 = new Producto("Zapatillas", 32000.00);
        Producto producto5 = new Producto("Bufanda", 4500.00);
        Producto producto6 = new Producto("Gorra", 3500.00);
        Producto producto7 = new Producto("Camisa", 12000.00);
        Producto producto8 = new Producto("Boxer", 3000.00);
        Producto producto9 = new Producto("Cinturón", 4000.00);
        Producto producto10 = new Producto("Medias", 1500.00);
        
        
        Orden orden1 = new Orden();
        // Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto8);
        orden2.mostrarOrden();

        Orden orden3 = new Orden();
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto1); 
        orden3.agregarProducto(producto4); 
        orden3.mostrarOrden();
        
        
        // Tarea
        // Crear mas objetos de tipo Productos = 10
        // Crear mas objetos de tipo Orden = 2
    }
}
