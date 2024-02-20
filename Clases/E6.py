class Auto ():

    def __init__(self, marca, color, modelo):

        self.marca = marca
        self.color = color
        self.modelo = modelo

    def mostrarAuto(self):

        return(f"El carro de marca {self.marca}, tiene un con color {self.color} y modelo {self.modelo}")

if __name__ == "__main__":

    logan = Auto("Renault", "Gris", 2010)
    cx30 = Auto("Mazda", "Blanco", 2016)
    swift = Auto("Suzuki", "Negro", 2023)

    print(logan.mostrarAuto())
    print(cx30.mostrarAuto())
    print(swift.mostrarAuto())


