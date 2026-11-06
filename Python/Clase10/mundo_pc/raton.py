from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones

    def __str__(self):
        return f"Id: {self.id_raton}, Marca: {self._marca}, Tipo de Entrada: {self._tipo_entrada}"

    # Hacemos pruebas
if __name__ == "__main__":
    raton1 = Raton("HP", "USB")
    print(raton1)

    raton2 = Raton("Acer", "Bluetooth")
    print(raton2)
