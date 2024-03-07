class Persona():

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):

        super().__init__(nombre, edad)

        self.sueldo = sueldo

    def mostrar(self):

        if self.sueldo >= 3000000:

            print(f"El nombre de la persona es: {self.nombre}, con una edad de: {self.edad}. Debe pagar impuesto debido a su sueldo")

        else:

            print(f"El nombre de la persona es: {self.nombre}, con una edad de: {self.edad}. No debe pagar impuesto debido a su sueldo")


emp1 = Empleado("Julian", 32, 5000000)

emp2 = Empleado("Josue", 30, 2800000)

emp1.mostrar()

emp2.mostrar()

