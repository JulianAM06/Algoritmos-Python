#Un almacén efectúa una promoción en la cual se hace un descuento sobre el valor de la compra total, según el color de la bolita que el cliente saque al pagar en caja. Si la bolita es blanca no se le hará descuento, si es verde se le hará un 10% de descuento, si es amarilla un 25%, si es azul un 50% y si es roja un 100%. Hacer un algoritmo para determinar la cantidad final que un cliente deberá pagar por su compra. Se sabe que solo hay bolitas de los colores mencionados.

def determinarBolita (numero):
    
    bolitas = {
        
        1: 'Blanca',
        2: 'Verde',
        3: 'Amarilla',
        4: 'Azul',
        5: 'Roja'
 
    }
    
    bolita = bolitas.get(numero, -1)
    return bolita



colorBolita = int(input("Ingrese\nBlanca--1\nVerde--2\nAmarilla--3\nAzul--4\nRoja--5\nPara conocer el color de la bolita: "))
valorCompra = int(input("Ingrese valor de la compra: "))


bolita = determinarBolita(colorBolita)


if bolita != -1:
    
    print(f"El color de la Bolita es {bolita}")
    
else:
    print("El numero ingresado no lo reconoce el Programa")    

    

if bolita == 'Blanca':
    
    valorCompraTotal = valorCompra
    

elif bolita == 'Verde':
    
    valorDescuento = valorCompra * 0.10
    
    valorCompraTotal = valorCompra - valorDescuento
    
elif bolita == 'Amarilla':
    
    valorDescuento = valorCompra * 0.25
    
    valorCompraTotal = valorCompra - valorDescuento
    
elif bolita == 'Azul':
    
    valorDescuento = valorCompra * 0.50
    
    valorCompraTotal = valorCompra - valorDescuento
    
elif bolita == 'Roja':
    
    valorCompraTotal = valorCompra - valorCompra
    
else:
    print("El color de la bolita no Existe")
    
    
print("El total a pagar es: ", valorCompraTotal)































"""def determinarBolita(letra):
    coloresBolitas = {
        'B': 'Blanca',
        'V': 'Verde',
        'A': 'Amarilla',
        'Z': 'Azul',
        'R': 'Roja'
    }
    colorBolita = coloresBolitas.get(letra, 1)
    return colorBolita


VC = float(input("Ingrese el valor de la compra: "))
letraBolita = input("Ingrese color de la bolita: \nBlanca--B\nVerde--V\nAmarilla--A\nAzul--Z\nRoja--R\nPara determinar el valor del descuento: ").upper()

colorBolita = determinarBolita(letraBolita)

if colorBolita != 1:
    print (f"El color de la bolita es: {colorBolita}")

else: 
    print ("La letra ingresada es desconocida para el programa")


if letraBolita == "B":
    VT = VC

elif letraBolita == "V":
    VT = VC - (VC * 0.10)

elif letraBolita == "A":
    VT = VC - (VC * 0.25)

elif letraBolita == "Z":
    VT = VC - (VC * 0.50)

elif letraBolita == "R":
    VT = VC - VC

print ("El valor total de la compra es: ",VT)"""