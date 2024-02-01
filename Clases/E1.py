class Coche():

    #Podemos crear un contructor inicial o Init 
    def __init__(self):
        
        #Propiedades de la Clase Coche, tambien pueden denominarse propiedades de estado inicial
        self.largoChasis = 250 
        self.anchoChasis = 120
        self.__ruedas = 4 #Se realiza el Encapsulamiento, lo cual no permite modificar esta propiedad por fuera de la clase => __ruedas
        self.enMarcha = False

    #Creamos un Metodo(Comportamientos)
    def arrancar (self, arrancamos):

        self.enMarcha = arrancamos

        if (self.enMarcha) == True:
            return "EL coche esta en marcha"

        else: 
            return "EL coche esta estacionado"
        
    def estado(self):

        print("El coche tiene ", self.__ruedas, " ruedas.", "Un ancho de: ", self.anchoChasis,", y un largo de: ", self.largoChasis)

            
        
        

#Creamos un Objeto e instanciamos la clase
miCoche = Coche()

#Llamamos al Metodo y le pasamos un segundo parametro
print(miCoche.arrancar(False))

#Para llamar la propiedad o atributo, ponemos nombre del objeto y luego un punto, luego el nombre de la propiedad
print(miCoche.largoChasis)

#Llammamos el otro Metodo
print(miCoche.estado())


print("---------------Creamos el segundo objeto-------------------")

miCoche2 = Coche()

print(miCoche2.arrancar(True))

print(miCoche2.largoChasis)

print(miCoche2.estado())

