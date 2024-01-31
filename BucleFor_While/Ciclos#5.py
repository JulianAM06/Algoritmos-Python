CA = int(input("Ingrese la cantidad de animales\nElefantes--4\nJirafas--6\nChimpance--8\na estudiar: "))

i = 0
TAE1 = 0
TAE2 = 0
TAE3 = 0


if CA > 0:
    
    for i in range(CA):
        
        Edad = float(input("Ingrese edad del animal: "))
        
        if Edad >= 0 and Edad <= 1:
            TAE1 = TAE1 + 1
            
        if Edad > 1 and Edad <=3:
            TAE2 = TAE2 +1 
            
        if Edad > 3:
            TAE3 = TAE3 + 1
            
    TA = TAE1 + TAE2 + TAE3
    
    PA1 = (TAE1/TA)*100
    PA2 = (TAE2/TA)*100
    PA3 = (TAE3/TA)*100
    
    
    print("El porcentaje de animales entre 0 & 1 año es: ",PA1)
    print("El porcentaje de animales entre 1 & 3 años es: ",PA2)
    print("El porcentaje de animales 3 años en adelante es: ",PA3)
    
    