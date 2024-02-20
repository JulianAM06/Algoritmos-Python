class Matematicas():

    def __init__(self, n1, n2):

        self.n1 = n1
        self.n2= n2

    def sumar (self):

        return self.n1 + self.n2
    
    def restar (self):

        return self.n1 - self.n2
        
        
    def multiplicar(self):

        return self.n1 * self.n2
    
    def dividir(self):

        if self.n2 == 0:

            return ("No se puede dividir entre cero")
        
        else:

            return self.n1 / self.n2
        
op1 = Matematicas(6, 0)

print(f"La suma es: {op1.sumar()}")
print(f"La resta es: {op1.restar()}")
print(f"La multiplicacion es: {op1.multiplicar()}")
print(f"La division es: {op1.dividir()}")

