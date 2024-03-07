class Cuenta():

    def __init__(self, titular, cantidad):

        self.titular = titular
        self.cantidad = cantidad

    
class CajaAhorro(Cuenta):

    def __init__(self, titular, cantidad):

        super().__init__(titular, cantidad)

    def mostrarCuenta(self):

        print(f"El titualar de la cuenta es: {self.titular} y su cuenta posee un valor de {self.cantidad}")



class PlazoFijo(Cuenta):

    def __init__(self, titular, cantidad, plazo, interes):

        super().__init__(titular, cantidad)

        self.plazo = plazo

        self.interes = interes

    def importeInteres(self,importe):

        self.importe = importe

    def mostrarInfo(self):

        if (self.importe):

            print(f"El nombre del titular es: {self.titular}, con un plazo de: {self.plazo} y un interes de: {self.interes}. El total del interes es: {(self.cantidad * self.interes) / 100}")

        else:

             print(f"El nombre del titular es: {self.titular}, con un plazo de: {self.plazo} y un interes de: {self.interes}")


per1 = CajaAhorro("Matias", 10000000)

per1.mostrarCuenta()

per2 = PlazoFijo("Matias", 10000000, 12, 1.2)

per2.importeInteres(False)

per2.mostrarInfo()