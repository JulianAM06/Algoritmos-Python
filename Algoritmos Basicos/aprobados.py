AA = int (input("Ingrese el numero de alumnos Aprobados "))
AD = int (input("Ingrese el numero de alumnos Desaprobados "))
AS = int (input("Ingrese el numero de alumnos Sobresalientes "))
AN = int (input("Ingrese el numero de alumnos Notables "))

TA = AA + AD + AS + AN

porcAA = (AA/TA)*100
porcAD = (AD/TA)*100
porcAS = (AS/TA)*100
porcAN = (AN/TA)*100

porcAG = ((TA - AD)/TA)*100

print ("La cantidad de Alumnos son: ",TA)
print ("El porcentaje de Alumnos Aprobados es: ", porcAA)
print ("El porcentaje de Alumnos Desaprobados es: ", porcAD)
print ("El porcentaje de Alumnos Sobresalientes es: ", porcAS)
print ("El porcentaje de Alumnos Notables es: ", porcAN)
print ("El porcentaje de Alumnos Ganadores es: ", porcAG)