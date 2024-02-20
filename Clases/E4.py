class Perro ():

    def __init__(self, raza, edad, color, tamaño):
        
        self.raza = raza
        self.edad = edad
        self.color = color
        self.tamaño = tamaño

    def mostrar (self):

        print(f"El perro tiene una raza {self.raza}, con una edad de {self.edad} años, un color {self.color} y un tamaño de {self.tamaño} metros")

if __name__ == "__main__":


    miperro1 = Perro("pitbull", 4, "Cafe", 1.55)
    miperro2 = Perro("chitzu", 2, "negro", 1.22)

    miperro1.mostrar()
    miperro2.mostrar()



