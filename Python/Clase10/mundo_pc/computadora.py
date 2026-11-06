class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
          {self._nombre} - Id: {self.id_computadora}
          Monitor: {self._monitor}
          Teclado: {self._teclado} 
          Raton: {self._raton}
        '''

if __name__ == "__main__":
    from monitor import Monitor
    from teclado import Teclado
    from raton import Raton

    monitor1 = Monitor("HP", "24 pulgadas")
    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("HP", "USB")

    computadora1 = Computadora("HP", monitor1, teclado1, raton1)
    print(computadora1)

    monitor2 = Monitor("Acer", "27 pulgadas")
    teclado2 = Teclado("Acer", "Bluetooth")
    raton2 = Raton("Acer", "Bluetooth")

    computadora2 = Computadora("Acer", monitor2, teclado2, raton2)
    print(computadora2)
