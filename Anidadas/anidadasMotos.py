nombre = input("Ingresa nombre del cliente: ")
moto = int(input("Ingresa\nMoto1--100cc, $2.900.000\nMoto2--110cc, 3.650.000\nMoto3--125cc, 4.000.000\nMoto4--250cc, 6.000.000\nPara saber la moto: "))
unidades = int(input("Ingresa cantidad de Motos compradas: "))

if unidades > 3:

    if moto == 1:

        valorMoto = 2900000 * unidades

        valorDescuento = valorMoto * 0.15

        valorTotal = valorMoto - valorDescuento

    elif moto == 2:

        valorMoto = 3650000 * unidades

        valorDescuento = valorMoto * 0.15

        valorTotal = valorMoto - valorDescuento

    elif moto == 3:

        valorMoto = 4000000 * unidades

        valorDescuento = valorMoto * 0.15

        valorTotal = valorMoto - valorDescuento

    elif moto == 4:

        valorMoto = 6000000 * unidades

        valorDescuento = valorMoto * 0.15

        valorTotal = valorMoto - valorDescuento

    print(f"{nombre} debe pagar {valorTotal}")

else:

    if moto == 1:

        valorMoto = 2900000 * unidades

        valorTotal = valorMoto - valorMoto

    elif moto == 2:

        valorMoto = 3650000 * unidades

        valorTotal = valorMoto

    elif moto == 3:

        valorMoto = 4000000 * unidades

        valorTotal = valorMoto 

    elif moto == 4:

        valorMoto = 6000000 * unidades

        valorTotal = valorMoto 

    print(f"{nombre} debe pagar {valorTotal}")


    

