x = int(input("Ingrese el tamaño de la serie de Fibonacci: "))

if x <= 0:

    print("Ingrese un tamaño válido mayor que cero")

else:

    serie = [0, 1]

    for i in range(2, x):

        serie.append(serie[-1] + serie[-2])

    print("La serie de Fibonacci es:", serie)

    # lista = [0, 1, 2, 3, 4, 5, 6]
    # lista = [55, 80, 98]

    