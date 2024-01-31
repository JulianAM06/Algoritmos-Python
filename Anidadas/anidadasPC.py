#Ver en el Taller

cantidadPC = int(input("Ingrese cantidad de PC: "))


if cantidadPC < 5:
    
    precioPC = 11000 * cantidadPC
    
    descuento = precioPC * 0.10
    
    precioConDescuento = precioPC - descuento


elif cantidadPC >= 5 and cantidadPC < 10:
    
    precioPC = 11000 * cantidadPC
    
    descuento = precioPC * 0.20
    
    precioConDescuento = precioPC - descuento


else:
    
    precioPC = 11000 * cantidadPC
    
    descuento = precioPC * 0.40
    
    precioConDescuento = precioPC - descuento
    
print("El Precio Total a Pagar de acuerdo a la cantidad de Computadores es: ", precioConDescuento)
    
    
































"""CC = float (input("Ingrese cantidad de computadores a comprar: "))

if CC < 5:
    VC = (CC * 11000) 
    VD = VC * 0.10
    CTC = VC - VD

elif CC >=5 and CC <10:
    VC = (CC * 11000) 
    VD = VC * 0.20
    CTC = VC - VD

else: 
    VC = (CC * 11000) 
    VD = VC * 0.40
    CTC = VC - VD

print ("El costo total de acuerdo a la cantidad de Computadoras es: ",CTC)"""