#Ver en el taller


CLL = int (input("Ingrese la cantidad de llantas a comprar: "))

if CLL < 5:
    VTLL = CLL * 300

elif CLL >= 5 and CLL <= 10:
    VTLL = CLL * 250

else: VTLL = CLL * 200

print ("El valor total segun la cantidad de lantas es: ",VTLL)