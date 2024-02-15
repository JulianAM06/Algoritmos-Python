class Cuenta():

    codigo = 1010
    tipo = "ahorro"
    saldo = 500
    movimiento = False

    def dinero (self):
        self.movimiento = True

    def transferencia (self):

        if(self.movimiento):

            return ("Se realizo la transferencia")
        
        else:

            return ("No se realizo la Transferencia")


cuenta1 = Cuenta()

print(f"El numero de cuenta es {cuenta1.codigo} es tipo {cuenta1.tipo} y su saldo actual es {cuenta1.saldo}")

cuenta1.dinero()

print(cuenta1.transferencia())
        

   