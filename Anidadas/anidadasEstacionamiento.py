horas = int(input("Ingresa horas: "))
minutos = int(input("Ingresa minutos: "))

if horas == 0:

    print(2000)

elif horas == 1:

    print(2000)

elif horas == 2 and minutos == 0:

    print(2000)

elif horas == 2 and minutos != 0:

    if minutos <= 30:

        print(2400)

    elif minutos >= 31 or minutos <= 59:

        print(2800)

elif horas == 3 and minutos == 0:

    print(2800)

elif horas == 3 and minutos != 0:

    if minutos <= 30:

        print(3200)

    elif minutos >= 31 or minutos <= 59:

        print(3600)

elif horas == 4 and minutos == 0:

    print(3600)

elif horas == 4 and minutos != 0:

    if minutos <= 30:

        print(4000)

    elif minutos >= 31 or minutos <= 59:

        print(4400)

elif horas == 5 and minutos == 0:

    print(4400)

elif horas == 5 and minutos != 0:

    if minutos <= 30:

        print(4800)

    elif minutos >= 31 or minutos <= 59:

        print(5200)