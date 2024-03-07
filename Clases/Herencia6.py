class Electrodomestico():

    def __init__(self, precioBase, peso, precioFinal):

        self.precioBase = precioBase
        
        self.peso = peso

        self.precioFinal = precioFinal

    def comprobarConsumoEnergetico(self, consumoEnergetico):

        self.consumoEnergetico = consumoEnergetico.upper()

        if self.consumoEnergetico == "A":

            self.consumoEnergetico = "A"

        elif self.consumoEnergetico == "B":

            self.consumoEnergetico = "B"

        elif self.consumoEnergetico == "C":

            self.consumoEnergetico = "C"

        elif self.consumoEnergetico == "D":

            self.consumoEnergetico = "D"

        elif self.consumoEnergetico == "E":

            self.consumoEnergetico = "E"

        elif self.consumoEnergetico == "F":

            self.consumoEnergetico = "F" 
        
        else:

            self.consumoEnergetico = "F"

    def comprobarColor(self, color):

        self.color = color.upper()

        if self.color == "BLANCO":

            self.color = "Blanco"

        elif self.color == "NEGRO":

            self.color = "Negro"

        elif self.color == "ROJO":

            self.color = "Rojo"

        elif self.color == "AZUL":
            
            self.color = "Azul"
        
        elif self.color == "GRIS":

            self.color = "Gris"

    def precioTotal(self):

        if self.consumoEnergetico == "A":

            if self.peso <= 19:

                self.precioFinal = self.precioBase + 100 + 10

            if self.peso >= 20 and self.peso <= 49:

                self.precioFinal = self.precioBase + 100 + 50

        elif self.consumoEnergetico == "B":

            if self.peso <= 19:

                self.precioFinal = self.precioBase + 80 + 10

            if self.peso >= 20 and self.peso <= 49:

                self.precioFinal = self.precioBase + 80 + 50

        elif self.consumoEnergetico == "C":

            if self.peso <= 19:

                self.precioFinal = self.precioBase + 60 + 10

            if self.peso >= 20 and self.peso <= 49:

                self.precioFinal = self.precioBase + 60 + 50

        elif self.consumoEnergetico == "D":

            if self.peso <= 19:

                self.precioFinal = self.precioBase + 50 + 10

            if self.peso >= 20 and self.peso <= 49:

                self.precioFinal = self.precioBase + 50 + 50

        elif self.consumoEnergetico == "E":

            if self.peso <= 19:

                self.precioFinal = self.precioBase + 30 + 10

            if self.peso >= 20 and self.peso <= 49:

                self.precioFinal = self.precioBase + 30 + 50

        elif self.consumoEnergetico == "F":

            if self.peso <= 19:

                self.precioFinal = self.precioBase + 10 + 10

            if self.peso >= 20 and self.peso <= 49:

                self.precioFinal = self.precioBase + 10 + 50

    def mostrar(self):

            print(f"Precio Base: {self.precioBase}, Color: {self.color}, Consumo Energetico: {self.consumoEnergetico}, Peso: {self.peso} Kg, Su precio final es: {self.precioFinal}")

class Lavadora(Electrodomestico):

    def __init__(self, precioBase, peso, precioFinal, carga):

        super().__init__(precioBase, peso, precioFinal)

        self.carga = carga

    def mostrar2(self):
            
        if self.carga > 30:

            print(f"Precio Base: {self.precioBase}, Color: {self.color}, Consumo Energetico: {self.consumoEnergetico}, Peso: {self.peso} Kg, Su precio final es: {self.precioFinal + 50}")

        else:

            print(f"Precio Base: {self.precioBase}, Color: {self.color}, Consumo Energetico: {self.consumoEnergetico}, Peso: {self.peso} Kg, Su precio final es: {self.precioFinal}")

class Televisor(Electrodomestico):

    def __init__(self, precioBase, peso, precioFinal, resolucion, sintonizadorTDT):

        super().__init__(precioBase, peso, precioFinal)

        self.resolucion = resolucion

        self.sintonizadorTDT = sintonizadorTDT

    def mostrar3(self):

        if self.resolucion > 40 and self.sintonizadorTDT == True:

            print(f"Precio Base: {self.precioBase}, Color: {self.color}, Consumo Energetico: {self.consumoEnergetico}, Peso: {self.peso} Kg, Su precio final es: {self.precioFinal + 50 + (0.30 * 150)}")
        
        elif self.sintonizadorTDT == True:

            print(f"Precio Base: {self.precioBase}, Color: {self.color}, Consumo Energetico: {self.consumoEnergetico}, Peso: {self.peso} Kg, Su precio final es: {self.precioFinal + 50}")
            

elec1 = Electrodomestico(100, 25, 0)

elec1.comprobarConsumoEnergetico("b")

elec1.comprobarColor("azul")

elec1.precioTotal()

elec1.mostrar()

lav2 = Lavadora(100, 25, 0, 35)

lav2.comprobarConsumoEnergetico("c")

lav2.comprobarColor("blanco")

lav2.precioTotal()

lav2.mostrar2()

tele3 = Televisor(100,25, 0, 30, True)

tele3.comprobarConsumoEnergetico("c")

tele3.comprobarColor("blanco")

tele3.precioTotal()

tele3.mostrar3()