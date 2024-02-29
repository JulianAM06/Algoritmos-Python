class Cuenta ():

    def __init__(self, saldoInicial):

        self.saldoInicial = saldoInicial

    def mostrarSaldo(self):

        if self.saldoInicial >= 0:

            print (f"El Saldo Inicial es: {self.saldoInicial}")
        
        else:

            self.saldoInicial = 0

            print (f"Saldo Inicial Invalido, se incia en: {self.saldoInicial}")

    def credito(self, agregar):

        self.agregar = agregar

        self.total = self.saldoInicial + self.agregar

        print("El Saldo actual es: ", self.total)

    def retirar(self, retiro):

        self.retiro = retiro

        self.actualizado = self.total - self.retiro

        print("El saldo actual es: ", self.actualizado)

    def obtenerSaldo (self):

        print(f"El saldo inicial es: {self.saldoInicial}, si ha realizado abonos, el saldo es: {self.total} y si se han hecho retiros es: {self.actualizado}")

C1 = Cuenta(2000)

C1.mostrarSaldo()
C1.credito(1000)
C1.retirar(500)
C1.obtenerSaldo()
