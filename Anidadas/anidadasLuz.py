# Mostrar el total a pagar de acuerdo el consumo de luz. Si es menos de 1000KW, la tarifa es del 1.2 x hora, entre 1000KW y 1850KW la tarifa es de 0.9 x hora, y mas de 1850KW la tarifa es de 0.7 x hora. La tarifa base es de 10 dolares.

consumoKW = int(input("Ingrese consumo de KW: "))
horasConsumo = int(input("Ingrese horas de consumo: "))


if consumoKW < 1000:
    
    totalPago = (1.2 * 10) * horasConsumo
    
elif consumoKW >= 1000 and consumoKW < 1850:
    
    totalPago = (0.9 * 10) * horasConsumo
    
else:
    
    totalPago = (0.7 * 10) * horasConsumo
    
print("El total a pagar de acuerdo al consumo es: ", totalPago)


    
    
    
    


































"""KW = float (input("Ingrese la cantidad de Kilo Watts "))
CH = float (input("Ingrese cantidad de horas "))
TB = float (input ("Ingrese la tarifa base "))

if KW < 1000:
    CTL = (CH * 1.2) * TB

elif KW >= 1000 and KW <=1850:
    CTL = (CH * 1) * TB

else:
    CTL = (CH * 0.9) * TB

print ("El Costo total de la luz es: ",CTL)"""