class Producto {
    static contadorProductos = 0;

    constructor(nombre, precio) {
        this.idProducto = ++Producto.contadorProductos;
        this.nombre = nombre;
        this.precio = precio;
    }

    // Método para obtenmer el id del producto
    getIdProducto() {
        return this.idProducto;
    }

    // Método para obtener el nombre del producto
    getNombre() {
        return this.nombre;
    }

    // Método para setear el nombre del producto
    setNombre(nombre) {
        this.nombre = nombre;
    }

    // Método para obtener el precio del producto
    getPrecio() {
        return this.precio;
    }

    // Método para setear el precio del producto
    setPrecio(precio) {
        this.precio = precio;
    }

    // Método para mostrar la información del producto
    toString() {
        return `Producto { id: ${this.idProducto}, nombre: ${this.nombre}, precio: $${this.precio} }`;
    }
}

const producto1 = new Producto("Teclado", 25000);
const producto2 = new Producto("Mouse", 12000);
const producto3 = new Producto("Monitor", 80000);
const producto4 = new Producto("Auriculares", 15000);
const producto5 = new Producto("Webcam", 20000);
// const producto6 = new Producto("Parlantes", 30000);

// Obtener los atributos del producto1
console.log(`Id del producto 1: ${producto1.getIdProducto()}`);
console.log(`Nombre del producto 1: ${producto1.getNombre()}`);
console.log(`Precio del producto 1: $${producto1.getPrecio()}`);

// Modificar los atributos
producto1.setNombre("Teclado mecánico");
producto1.setPrecio(30000);

// Mostrar la información completa del producto1
console.log(`Información del producto 1: ${producto1.toString()}`);

// Obtener los atributos del producto2
console.log(`Id del producto 2: ${producto2.getIdProducto()}`);
console.log(`Nombre del producto 2: ${producto2.getNombre()}`);
console.log(`Precio del producto 2: $${producto2.getPrecio()}`);

// Mostrar la información completa del producto2
console.log(`Información del producto 2: ${producto2.toString()}`);

// Consultar el contador estático
console.log(`Cantidad de productos creados: ${Producto.contadorProductos}`);



class Orden {
    static contadorOrdenes = 0;
    static MAX_PRODUCTOS = 5;

    constructor() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = [];
    }

    // Método para agregar un producto a la orden
    agregarProducto(producto) {
        if (this.productos.length < Orden.MAX_PRODUCTOS) {
            this.productos.push(producto);
        } else {
            console.log("No se pueden agregar más productos a la orden.");
        }
    }

    // Método para calcular el total de la orden
    calcularTotal() {
        let total = 0;
        for (let producto of this.productos) {
            total += producto.getPrecio();
        }
        return total;
    }

    // Método para mostrar la información de la orden
    mostrarOrden() {
        let productosStr = "";
        for (let producto of this.productos) {
            productosStr += producto.toString() + " ";
        }
        return `Orden { id: ${this.idOrden}, total: $${this.calcularTotal()} } Productos: ${productosStr}`;
    }
}

// Ejemplo de uso con tus productos
const orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto4);
orden1.agregarProducto(producto5);
//orden1.agregarProducto(producto6); // Intento de agregar un sexto producto (no se agregará)

console.log(orden1.mostrarOrden());
console.log(`Cantidad de órdenes creadas: ${Orden.contadorOrdenes}`);



class VentasTest {
    static main() {
        // Crear los productos
        const producto1 = new Producto("Teclado", 25000);
        const producto2 = new Producto("Mouse", 12000);
        

        // Crear una orden
        const orden1 = new Orden();

        // Agregar los productos a la orden
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);

        // Mostrar la información de la orden
        console.log(orden1.mostrarOrden());

        // Mostrar la cantidad de órdenes creadas
        console.log(`Cantidad de órdenes creadas: ${Orden.contadorOrdenes}`);
    }
}

// Ejecutar la prueba
VentasTest.main();
