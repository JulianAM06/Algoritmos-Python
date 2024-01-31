FC = float (input("Ingrese valor de la Fianza"))

if FC <= 500000:
    CC = (FC*0.03)
else: CC = (FC*0.02)

print ("La cuota a pagar es: ",CC)