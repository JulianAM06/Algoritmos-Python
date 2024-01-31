def determinarZona (numero):
    zonas = {
        12: 'America del Norte',
        15: 'America Central',
        18: 'America del Sur',
        19: 'Europa',
        23: 'Asia',
        25: 'Africa',
        29: 'Oceania'
    }
    zona = zonas.get (numero,0)
    return zona


numZona = int (input("Ingrese el numero\nAmerica del Norte--12\nAmerica Central--15\nAmerica del Sur--18\nEuropa--19\nAsia--23\nAfrica--25\nOceania--29\nPara conocer la zona destino de la llamada: "))
CM = int (input("Ingrese cantidad de minutos: "))

zona = determinarZona(numZona)


if zona !=0:
    print (f"La zona seleccionada para la llamada es: {zona}")

else:
    print ("El numero ingresado es desconocido para el programa")

if numZona ==12:
    VLL = CM * 2

elif numZona ==15:
    VLL = CM * 2.2

elif numZona ==18:
    VLL = CM * 4.5

elif numZona ==19:
    VLL = CM * 3.5

elif numZona ==23:
    VLL = CM * 6

elif numZona ==25:
    VLL = CM * 6

elif numZona ==29:
    VLL = CM * 5

print ("El valor total de la llamda de acuerdo a la zona y la cantidad de minutos es: ",VLL)