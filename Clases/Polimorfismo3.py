class DemasiadoRapidoException(Exception):
    pass

class Vehiculo:
    def __init__(self, matricula):
        self.matricula = matricula
        self.velocidad = 0

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def __str__(self):
        return f"Matrícula: {self.matricula}, Velocidad: {self.velocidad} km/h"


class Coche(Vehiculo):
    def __init__(self, matricula, num_puertas):
        super().__init__(matricula)
        self.num_puertas = num_puertas

    def obtener_num_puertas(self):
        return self.num_puertas

    def __str__(self):
        return super().__str__() + f", Número de puertas: {self.num_puertas}"


class Remolque:
    def __init__(self, peso):
        self.peso = peso

    def __str__(self):
        return f"Remolque - Peso: {self.peso} kg"


class Camion(Vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.remolque = None

    def pon_remolque(self, remolque):
        self.remolque = remolque

    def quita_remolque(self):
        self.remolque = None

    def acelerar(self, cantidad):
        if self.remolque and self.velocidad + cantidad > 100:
            raise DemasiadoRapidoException("El camión con remolque no puede superar los 100 km/h")
        super().acelerar(cantidad)

    def __str__(self):
        if self.remolque:
            return super().__str__() + f", {self.remolque}"
        else:
            return super().__str__()

coche = Coche("1234ABC", 4)
coche.acelerar(50)
print(coche)

camion = Camion("5678XYZ")
remolque = Remolque(2000)
camion.pon_remolque(remolque)
camion.acelerar(40)
print(camion)