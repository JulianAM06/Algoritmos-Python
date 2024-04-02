dia = int(input("Ingresa dia: "))
mes = int(input("Ingresa mes: "))
año = int(input("Ingresa año: "))

if mes == 1:

    if dia == 31:

        print(f"Mañana sera 01 2 {año}")

    elif dia >= 1 or dia <= 30:

        mañana = dia + 1

        print(f"Mañana sera {mañana} {mes} {año}")

elif mes == 2:

    if dia == 28:

        print(f"Mañana sera 01 3 {año}")

    elif dia >= 1 or dia <= 27:

        mañana = dia + 1

        print(f"Mañana sera {mañana} {mes} {año}")

elif mes == 12:

    if dia == 31:

        añoNuevo = año + 1

        print(f"Mañana sera 01 1 {añoNuevo}")

    elif dia >= 1 or dia <= 30:

        mañana = dia + 1

        print(f"Mañana sera {mañana} {mes} {año}")

    

