comprobar = True

while comprobar == True:
    
    n = int (input("Ingrese cantidad de variables: "))
    
    if n > 0:
        comprobar = False
        Resultado = 0
        j = 0
        
        for i in range (n):
            
            j = int (input("Ingrese numero: "))
            
            Resultado = (j + j)/n
            
           
        print(Resultado)
            
    else:
        print("Dato incorrecto...Intenta nuevamente") 
    
