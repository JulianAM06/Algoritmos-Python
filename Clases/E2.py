class Alumno():

    #Metodo Contructor Inicial
    def __init__(self, nombre, nota):

        self.nombre = nombre
        self.nota = nota

    #Metodos
    def mostar(self):

        print(f"El nombre del estudiante es: {self.nombre} y su nota es: {self.nota}")

    def valoracion (self):

        if self.nota >= 3:

            print(f"El estudiante {self.nombre} ha Ganado")

        else: 

            print(f"El estudiante {self.nombre} ha Perdido")

if __name__ == "__main__":

    #Objetos  # Instancia de la clase
    alumno1 = Alumno("Julian", 4) 
    alumno2 = Alumno("Matias", 5)
    alumno3 = Alumno("Roberto", 2.8)

    #Metodos y Atributos de la clase, llamados
    alumno1.mostar()
    alumno1.valoracion()

    alumno2.mostar()
    alumno2.valoracion()

    alumno3.mostar()
    alumno3.valoracion()