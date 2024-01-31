SEXO = int (input("Ingrese su Sexo 1.Masculino 2.Femenino"))
EDAD = int (input("Ingrese Edad"))


if SEXO==1:
    PULM = (210-EDAD)/10
    print ("Las pulsaciones son: ",PULM)

else:
    PULF = (220-EDAD)/10
    print ("Las pulsacion son: ",PULF)
