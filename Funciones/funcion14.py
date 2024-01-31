def CalcularOperacion(n1, n2, op):
    
    
    if op == 1:
        Sum = n1 + n2
        return Sum
    elif op == 2:
        Res = n1 - n2
        return Res
    elif op == 3:
        Mul = n1 * n2
        return Mul
    elif op == 4:
        Div = n1 / n2
        return Div
    elif op == 5:
        Pot = n1 ** n2
        return Pot
    elif op == 6:
        Rad = n1 **(1/n2)
        return round(Rad,2)
        




comprobar = True

while comprobar ==True:
    
    n1 = float(input("Ingrese primer numero: "))
    n2 = float(input("Ingrese segundo numero: "))
    op = int(input("Ingrese\nSuma--1\nResta--2\nMultiplicacion--3\nDivision--4\nPotencia--5\nRadicacion--6\nPara saber la operacion a ejecutar: "))
    CO = CalcularOperacion(n1, n2, op)
    
    
    if op ==1 or op==2 or op==3 or op==4 or op==5 or op==6:

        comprobar = False
        print("El resultado es: ",CO)
    
    else:
        print("Ingresa un numero valido al del menu para saber la operacion a ejecutar")