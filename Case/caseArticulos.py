#Ver en el Taller


def determinarARt(letra):
    articulos = {
        'M':'Manzana',
        'U':'Uva',
        'P':'Papaya',
        'F':'Fresa',
        'B':'Banano',
        'A':'Aguacate'
    }
    articulo = articulos.get (letra, 0)
    return articulo


letraArt = input("Ingrese una letra \nManzana--M\nUva--U\nPapaya--P\nFresa--F\nBanano--B\nAguacate--A\nPara mostrar la fruta a comprar: ").upper()
precioIni = float(input("Ingrese precio original de la fruta: "))
numClave = int (input("Ingrese \nDescuento del 10%--1\nDescuento del 20%--2\nPara conocer el valor del descuento: "))

articulo = determinarARt (letraArt)

if articulo !=0:
    print(f"El articulo seleccionado es: {articulo}")

else: 
    print("La letra ingresada es desconocida para el programa")

if numClave ==1:
    VD = precioIni * 0.10
    VTD = precioIni - VD

elif numClave ==2:
    VD = precioIni * 0.20
    VTD = precioIni - VD

else:
    print("El numero ingresado no es un descuento reconocido por el sistema")

print ("El valor original del producto es: ",precioIni)
print ("El valor con el descuento seleccionado es: ",VTD)