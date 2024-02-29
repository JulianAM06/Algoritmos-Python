class Factura():

    def __init__(self, numPieza, descripcion, cantidad, precio):

        self.numPieza = numPieza
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def mostrar(self):

        print(f"Numero de Pieza: {self.numPieza}, la descripcion de la pieza es: {self.descripcion}, la cantidad actual es: {self.cantidad} y el valor unitario es: {self.precio}")

    def obtenerMontoFactura(self):

        if self.cantidad > 0:

            print("Total de la Factura: ", self.cantidad * self.precio)

        else:

            print("No hay Inventario")

F1 = Factura(1, "Broca Tugsteno para perforaciones en Concreto", 5, 10000)

F1.mostrar()
F1.obtenerMontoFactura()

