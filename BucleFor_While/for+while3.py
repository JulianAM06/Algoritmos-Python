comprobar = True

while comprobar == True:


    n = int (input("Ingrese cantidad de variables a recibir: "))

    if n > 0:
        comprobar = False
        positivo = 0
        negativo = 0
        nulo = 0
       
    
        for i in range(n):
            dato = int (input("Ingrese numero natural: "))
        
            if dato > 0:
                positivo +=1
            elif dato < 0:
                negativo +=1
            else:
                nulo =+1
            
        print ("La cantidad de numeros positivos son: ",positivo)
        print ("La cantidad de numeros negativos son: ", negativo)
        print ("La cantidad de nulos son: ", nulo)
    
    else:
        print("Ingresa dato correcto")