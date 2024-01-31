def determinarModelo (numero):
    
    modelos = {
        
        1: 'Cutlass',
        2: 'Cavalier',
        3: 'Chevy',
        4: 'Century'
        
    }
    
    modelo = modelos.get(numero, 0)
    return modelo


modeloCarro = int(input("Ingrese\nCutlass--1\nCavalier--2\nChevy--3\nCentury--4\nPara conocer el modelo a Comprar: "))
valorCarro = int(input("Ingrese el valor del Carro: "))

modelo = determinarModelo(modeloCarro)

if modelo != 0:
    print(f"El modelo del carro es {modelo}")
    
else:
    print("El numero ingresado no existe")
    

if modelo == 'Cutlass':
    
    valorDescuento = valorCarro * 0.08
    valorTotalCarro = valorCarro - valorDescuento
    
elif modelo == 'Cavalier':
    
    valorDescuento = valorCarro * 0.05
    valorTotalCarro = valorCarro - valorDescuento
    
elif modelo == 'Chevy':
    
    valorDescuento = valorCarro * 0.06
    valorTotalCarro = valorCarro - valorDescuento
    
elif modelo == 'Century':
    
    valorDescuento = valorCarro * 0.09
    valorTotalCarro = valorCarro - valorDescuento
    
else:
    
    print("El modelo del Carro no existe")
    
print("El valor Total del Carro de acuerdo al modelo y su descuento es: ",valorTotalCarro)




































"""def determinarModelo (numero):
    modelos = {
        1: 'Cutlass',
        2: 'Cavalier',
        3: 'Chevy',
        4: 'Century'
    }
    modelo = modelos.get (numero, 0)
    return modelo



numModelo = int (input("Ingrese numero\nCutlass--1\nCavalier--2\nChevy--3\nCentury--4\nPara indicar el modelo del carro seleccionado: "))
PI = float (input("Ingrese precio original del carro seleccionado: "))

modelo = determinarModelo(numModelo)


if modelo !=0:
    print (f"El modelo seleccionado es: {modelo}")

else:
    print ("El modelo no es valido")

if numModelo ==1:
    VT = PI - (PI * 0.08)

elif numModelo ==2:
    VT = PI - (PI * 0.05)

elif numModelo ==3:
    VT = PI - (PI * 0.06)

elif numModelo ==4:
    VT = PI - (PI * 0.09)

print ("El valor total a pagar con descuento es: ",VT)"""
