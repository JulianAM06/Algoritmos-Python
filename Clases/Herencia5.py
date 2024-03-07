class Persona():

    def __init__(self, nombre, edad, dni, sexo, peso, altura):

        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo.lower()
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):

        self.IMC = self.peso / (self.altura * self.altura)

        if self.IMC < 20:

            print("Falto de Peso")

        elif self.IMC >= 20 and self.IMC <= 25:

            print("Peso Ideal")

        else:

            print("Sobrepeso")

    def esMayor(self):

        if self.edad >= 18:

            print("Es mayor de Edad")

        else:

            print("Es menor de Edad")

    def validarSexo(self):

        if self.sexo == "m":

            print("Es Masculino")

        else:

            print("Es Femenina")

    def string(self):

        if self.sexo == "m":

            print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}, Sexo: Masculino, Peso: {self.peso} y Estatura: {self.altura}")

        else:

            print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}, Sexo: Femenino, Peso: {self.peso} y Estatura: {self.altura}")


p1 = Persona("Julian", 32, 1035425685, "M", 82, 1.78)

p1.calcularIMC()

p1.esMayor()

p1.validarSexo()

p1.string()

nombre = input("Ingresa nombre: ")

edad = int(input("Ingresa edad: "))

dni = int(input("Ingresa DNI: "))

sexo = input("Ingresa\nM--Masculino\nF--Femenino\nPara conocer su sexo: ")

peso = float(input("Ingresa peso: "))

altura = float(input("Ingresa altura: "))

p2 = Persona(nombre, edad, dni, sexo, peso, altura)

p2.calcularIMC()

p2.esMayor()

p2.validarSexo()

p2.string()

