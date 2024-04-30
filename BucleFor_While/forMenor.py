x = int(input("Ingresa la cantidad de numeros a registrar: "))

if x > 1:

    lista = []

    for i in range (0, x):

        n = int(input("Ingresa numero a validar: "))

        lista.append(n)

    print(min(lista))

else:

    print("No Aplica")


    # for i in range (incio ciclo, fin ciclo, paso del ciclo)
    # for i in range (0, 100, 2)

    