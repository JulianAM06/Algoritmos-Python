Ndias = int (input("Ingrese cantidad de dias a evaluar: "))


if Ndias > 0:
   
    for i in range(Ndias):
        TMax = float (input("Ingrese la temperatura maxima: "))
        TMin = float (input("Ingrese la temperatura minima: "))
        
        TPromedio = (TMax + TMin)/2
        
        print("la temperatura promedio es: ",TPromedio)
    
else:
    print("La cantidad de dias es incorrecta. Intente nuevamente")