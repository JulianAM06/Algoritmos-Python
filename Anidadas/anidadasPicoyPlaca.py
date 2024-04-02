digito = int((input("Ingresa la placa: "))[-1])

dia = input("Ingresa dia a validar: ").upper()

if dia == "LUNES":

    if digito == 0 or digito == 1 or digito == 2 or digito == 3:

        print("No puedes usar el Carro")

    else:

        print("Puedes usar el Carro")

if dia == "MARTES":

    if digito == 4 or digito == 5 or digito == 6 or digito == 7:

        print("No puedes usar el Carro")

    else:

        print("Puedes usar el Carro")

if dia == "MIERCOLES":

    if digito == 8 or digito == 9 or digito == 0 or digito == 1:

        print("No puedes usar el Carro")

    else:

        print("Puedes usar el Carro")

if dia == "JUEVES":

    if digito == 2 or digito == 3 or digito == 4 or digito == 5:

        print("No puedes usar el Carro")

    else:

        print("Puedes usar el Carro")

if dia == "VIERNES":

    if digito == 6 or digito == 7 or digito == 8 or digito == 9:

        print("No puedes usar el Carro")

    else:

        print("Puedes usar el Carro")


    

