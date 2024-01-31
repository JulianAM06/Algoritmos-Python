CHN = float (input("Ingrese cantidad de Horas Normales"))
CHE = float (input("Ingrese cantidad de Horas Extras"))
VHN = float (input("Ingrese valor de la Hora Normal Laboral"))

VHE = (VHN*0.75)+VHN

SHN = VHN*CHN
SHE = VHE*CHE

ST = SHN+SHE

print ("El salario Total es: ",ST)