from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto) # Esto es para agregar un nuevo producto

    def calcular_total(self):
        total = 0 # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()+' | '
        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalón', 150.00)
    productos1 = [producto1, producto2] # Lista de productos
    orden1 = Orden(productos1) # Primer objeto orden pasando la lista de productos
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)

    # Tarea: Modificar la orden2, ingresando nuevos productos con sus nombres y precios
    # crear una nueva lista de productos y agregarla a la orden2

    # Creamos nuevos objetos Producto
    producto3 = Producto('Zapatillas', 250.00)
    producto4 = Producto('Campera', 300.00)

    # Creamos una nueva lista de productos
    productos2 = [producto3, producto4]

    # Agregamos los nuevos productos a orden2
    for producto in productos2:
        orden2.agregar_producto(producto)

    # Mostramos la orden2 modificada
    print('\nOrden 2 modificada:')
    print(orden2)

