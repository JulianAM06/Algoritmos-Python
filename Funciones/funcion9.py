def CalcularIVA (n):
    return (VC*n)

VC = float(input("Ingrese valor de la compra: "))


VI = CalcularIVA(n=0.19)

VT = VC + VI

print("El valor total de la compra es: ",VT)