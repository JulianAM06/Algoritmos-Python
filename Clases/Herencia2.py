class Persona():

    #Constructor Principal de la clase Padre
    def __init__(self, apeP, apeM, nombres):

        self.apellidoPaterno = apeP
        self.apellidoMaterno = apeM
        self.nombres = nombres

    #Metodo de la clase Padre
    def mostrarNombreCompleto(self):

        return self.nombres + " " + self.apellidoPaterno + " " + self.apellidoMaterno

#Clase Hija heredando de la Clase Padre
class Estudiante(Persona):
    
    #En el constructor de la clase hija se pasa como parametros los atributos de la clase padre
    def __init__(self, apeP, apeM, nombres, carr):

        #Se realiza la llamada al constructor de la clase padre
        super().__init__(apeP, apeM, nombres)

        #Atributo propio de la clase hija
        self.carrera = carr

#Clase Hija heredando de la Clase Padre
class Profesor(Persona):

    #En el constructor de la clase hija se pasa como parametros los atributos de la clase padre
    def __init__(self, apeP, apeM, nombres, prof):

        #Se realiza la llamada al constructor de la clase padre
        super().__init__(apeP, apeM, nombres)

        #Atributo propio de la clase hija
        self.profesion = prof


#Instanciamos el Objeto con la clase hija
estud1 = Estudiante("Alzate", "Monsalve", "Julian", "Estudiante Desarrollo de Software")

#Instanciamos el Objeto con la clase hija
prof1 = Profesor("Martinez", "Correa", "Tomas", "Profesor de Ingenieria Civil")

print(estud1.mostrarNombreCompleto())

print(estud1.carrera)

print(prof1.mostrarNombreCompleto())

print(prof1.profesion)