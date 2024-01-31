#El centro comercial “Presto”, tiene una promoción con un descuento del 15% por el consumo de tres productos cuyo costo sea mayor a S/. 20000. Tener en cuenta que el descuento es sobre el valor total de los tres productos.


producto1 = int(input("Ingrese valor del Producto 1: "))
producto2 = int(input("Ingrese valor del Producto 2: "))
producto3 = int(input("Ingrese valor del Producto 3: "))

totalProductos = producto1 + producto2 + producto3


if totalProductos > 20000:
        
        descuento = totalProductos * 0.15
        
        totalPago = totalProductos - descuento
        
        print("El valor a pagar es: ",totalPago)
        
else:
        
        print("La suma de tus productos no tiene descuento")
    




































"""PR1 = float (input("Ingrese el costo del Producto 1"))
PR2 = float (input("Ingrese el costo del Producto 2"))
PR3 = float (input("Ingrese el costo del Producto 3"))

SumaPR = PR1+PR2+PR3

if SumaPR > 20000:
    VD = SumaPR*0.15
    VT = SumaPR-VD
    print ("El valor total es: ",VT)"""