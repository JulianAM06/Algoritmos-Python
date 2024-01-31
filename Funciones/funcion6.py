n = float(input("Ingrese valor de compra: "))
x = float(input("Ingrese valor IVA a calcular: "))


def calcularTotal (monto, IVA):
    
    IVA = x / 100
    Total = (monto * IVA) + monto
    
    return Total
    
print(calcularTotal(monto=n, IVA=x))
    