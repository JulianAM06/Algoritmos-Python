class Carro():

    def Desplazamiento(self):

        print("Me desplazo usando 4 ruedas")

class Moto():

    def Desplazamiento(self):

        print("Me desplazo usando 2 ruedas")

class Camion():

    def Desplazamiento(self):

        print("Me desplazo usando 6 ruedas")

# Normalmente se haria de esta manera para crear objetos y metodos para cada uno

miVehuculo1 = Moto()

miVehuculo1.Desplazamiento()

miVehiculo2 = Carro()

miVehiculo2.Desplazamiento()

miVehiculo3 = Camion()

miVehiculo3.Desplazamiento()

# Con Polimorfismo

def desplazamientoVehiculo(vehiculo):

    vehiculo.Desplazamiento()

miVehiculo4 = Camion()

desplazamientoVehiculo(miVehiculo4)

