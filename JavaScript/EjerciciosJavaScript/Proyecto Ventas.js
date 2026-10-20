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