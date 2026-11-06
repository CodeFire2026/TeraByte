 
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado
from orden import orden

monitor1 = Monitor("HP", "24 pulgadas")
teclado1 = Teclado("HP", "USB")
raton1 = Raton("HP", "USB")
computadora1 = Computadora("HP", monitor1, teclado1, raton1)


monitor2 = Monitor("Acer", "27 pulgadas")
teclado2 = Teclado("Acer", "Bluetooth")
raton2 = Raton("Acer", "Bluetooth")
computadora2 = Computadora("Acer", monitor2, teclado2, raton2)


computadoras1 = [computadora1, computadora2]
orden1 = orden(computadoras1)
print(orden1)
monitor3 = Monitor("Gamer", "18 pulgadas")
teclado3 = Teclado("Gamer", "Bluetooth")
raton3 = Raton("Gamer", "Bluetooth")
computadora3 = Computadora("Gamer", monitor3, teclado3, raton3)


monitor4 = Monitor("Logitech", "27 pulgadas")
teclado4 = Teclado("Logitech", "Bluetooth")
raton4 = Raton("Logitech", "Bluetooth")
computadora4 = Computadora("Logitech", monitor4, teclado4, raton4)

monitor5 = Monitor("Samsung", "27 pulgadas")
teclado5 = Teclado("Samsung", "Bluetooth")
raton5 = Raton("Samsung", "Bluetooth")
computadora5 = Computadora("Samsung", monitor5, teclado5, raton5)

computadora6 = Computadora("Samsung", monitor1, teclado2, raton4)
computadora7 = Computadora("Logitech", monitor2, teclado3, raton5)


computadoras1 = [computadora1, computadora2, computadora7, computadora4]
orden1 = orden(computadoras1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora3, computadora5, computadora6]
orden2 = orden(computadoras2)
orden2.agregar_computadora(computadora1)
print(orden2)

