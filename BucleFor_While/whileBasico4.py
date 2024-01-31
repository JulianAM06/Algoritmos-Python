cTotal = int (input("Ingrese cantidad de estudiantes: "))

i = 0
cH = 0
cM = 0
porcH = 0
porcM = 0 

if cTotal > 0:

    while cTotal > i:
        
        Sex = int (input("Ingrese 1--Hombre o 2--Mujer: "))
        
        if Sex == 1:
            cH = cH + 1
            porcH = (cH/cTotal)*100
            
        elif Sex ==2:
            cM = cM + 1
            porcM = (cM/cTotal)*100

        i = i + 1
                
    print("La cantidad total de estudiantes es: ",cTotal)
    print("La cantidad de Hombres es: ",cH)
    print("La cantidad de Mujeres es: ",cM)
    print("El porcentaje de Hombres es: ",porcH)
    print("El porcentaje de Mujeres es: ",porcM)