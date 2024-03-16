class Estudiante():

    def describir(self):

        print("Soy un buen Estudiante")

class Docente():

    def describir(self):

        print("Me dedico a enseñar Cursos")


class Trabajador():

    def describir(self):

        print("Trabajo dentro de una gran Empresa")

def describirPersona(persona):

    persona.describir()

doc1 = Docente()

describirPersona(doc1)