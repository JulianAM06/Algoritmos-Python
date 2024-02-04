class vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False  

    def enmarcha(self):

        self.enmarcha = True

    def acelera(self):

        self.acelera = True

    def frena(self):

        self.frena = True

    def estado(self):

        print("Marca: ", self.marca,  "\nModelo: ", self.modelo, "\nEnmarcha: ", self.enmarcha, 
              "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)


class Furgon(vehiculos):

    def carga(self, cargar):
        self.cargado = cargar

        if (self.cargado):
            return("El furgon esta cargado")

        else:
            return("El furgon no esta cargado")

        
class Moto(vehiculos):
    pique = ""

    def pique(self):
        self.pique = "Hacer pique"

        print("Marca: ", self.marca,  "\nModelo: ", self.modelo, "\nEnmarcha: ", self.enmarcha, 
              "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\n", self.pique)

miMoto = Moto("Yamaha", "Nmax")

miMoto.pique()

miMoto.estado()

miFurgon = Furgon("Renault", "Kangoo")

miFurgon.estado()

print(miFurgon.carga(True))

