def determinarMes(numero):
    meses = {
        1: 'Septiembre',
        2: 'Julio',
        3: 'Enero',
        4: 'Marzo',
        5: 'Noviembre',
        6: 'Febrero',
        7: 'Junio',
        8: 'Octubre',
        9: 'Marzo',
        10: 'Agosto',
        11: 'Mayo',
        12: 'Abril'
    }
    Mes = meses.get(numero, 0)
    return Mes


numMes = int (input("Ingrese numero \nSeptiembre--1\nJulio--2\nEnero--3\nMarzo--4\nNoviembre--5\nFebrero--6\nJunio--7\nOctubre--8\nMarzo--9\nAgosto--10\nMayo--11\nAbril--12\nPara mostrar al mes del año que correspone: "))

Mes = determinarMes (numMes)


if Mes != 0:
    print (f"El mes seleccionado es: {Mes}")

else: 
    print("El numero ingresado es desconocido por el programa")

