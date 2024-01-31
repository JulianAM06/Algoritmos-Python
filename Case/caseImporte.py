def determinarVehiculo(numero):
    vehiculos = {
        1: 'Bicicleta',
        2: 'Moto',
        3: 'Carro',
        4: 'Camion',
        5: 'Salir'
    }
    vehiculo = vehiculos.get(numero, -1)
    return vehiculo



numVehiculo = int (input("Ingrese numero\nBicicleta--1\nMoto--2\nCarro--3\nCamion--4\nSalir--5\nPara conocer su importe a pagar: "))
KM = float (input("Ingrese la cantidad de Kilometros a recorrer: "))
TM = float (input("Para Bicicletas,Motos o Carros poner 0, Si su vehiculo es un camion, ingrese el peso en toneladas: "))

vehiculo = determinarVehiculo(numVehiculo)


if vehiculo != -1:
    print(f"El vehiculo seleccionado es: {vehiculo}")

else:
    print("El numero seleccionado no es reconocido por el sistema")

if numVehiculo ==1 and TM == 0:
    VI = 100

elif numVehiculo ==2 and TM ==0:
    VI = KM * 30

elif numVehiculo ==3 and TM ==0:
    VI = KM * 30

elif numVehiculo ==4:
    VKM = KM * 30
    VTM = TM * 25
    VI = VKM + VTM

elif numVehiculo ==5:
    print("Hasta la proxima")

print ("El valor del importe es: ",VI)