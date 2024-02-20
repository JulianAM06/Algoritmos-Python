class Persona ():

    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad

    def saludar (self, otra_persona):

        return("Hola " + otra_persona.nombre  + " me llamo " + self.nombre + " y tengo " + str(self.edad) + " años")
    
juan = Persona("Juan", 32)

carolina = Persona("Carolina", 35)

print(juan.saludar(carolina))