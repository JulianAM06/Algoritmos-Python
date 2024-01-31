CHD = float (input("Ingrese cantidad de horas que estuvo dormido: "))
CHS = float (input("Ingrese cantidad de horas que estuvo sentado: "))
KG = float (input("Ingrese peso de la persona: "))


if KG ==70:
    CLD = (1.08 * 60) * CHD
    CLS = (1.66 * 60) * CHS

print ("La cantidad de calorias que consume estando dormido son: ",CLD)
print ("La cantidad de calorias que consume estando sentado son: ",CLS)

