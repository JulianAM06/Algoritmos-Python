comprobarN = True

while comprobarN == True:

    n = int (input("Ingrese cantidad de personas a evaluar: "))


    if n > 0:
        altHombres = 0
        pesoHombres = 0
        altMujeres = 0
        pesoMujeres = 0
        cantHombres = 0
        cantMujeres = 0
        comprobarN = False
        
        for i in range(n):
            peso = float(input("Ingrese peso en KG: "))
            altura = float (input("Ingrese altura en CM: "))
            
            comprobarG = True
            
            while comprobarG == True:
            
                genero = input("Ingrese genero Masculino (M) o Femenino (F): ")
                
        
                
                if genero.upper() == "M":
                    altHombres = altHombres + altura
                    pesoHombres = pesoHombres + peso
                    cantHombres +=1
                    comprobarG = False
                    
                elif genero.upper() == "F":
                    altMujeres = altMujeres + altura
                    pesoMujeres = pesoMujeres + peso
                    cantMujeres +=1
                    comprobarG = False
                    
                else:
                    print("El genero seleccionado no es correcto. Intente nuevamente")
                    

        
        promPesoH = 0
        promAltH = 0
        
        if cantHombres >0:  
            
            promPesoH = (pesoHombres/cantHombres)
            promAltH = (altHombres/cantHombres)
        
        promPesoM = 0
        promAltM = 0
            
        if cantMujeres >0:
            
            promPesoM = (pesoMujeres/cantMujeres)
            promAltM = (altMujeres/cantMujeres)
        
        print ("El promedio de altura en hombres es: ", promAltH)
        print ("El promedio de peso en hombres es: ", promPesoH)
        print ("EL promedio de altura en mujeres es: ", promAltM)
        print ("El promedio de peso en mujeres es: ",promPesoM)
        
        
    else:
        print("Ingrese dato correcto")