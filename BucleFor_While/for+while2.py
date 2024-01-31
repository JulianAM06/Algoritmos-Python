comprobar = True

while comprobar == True:

    num = int (input("Ingrese numero entero positivo: "))

    if num > 0:
        resultado = 0
        comprobar = False
        for i in range (1,num +1):
            resultado = resultado + (1/i)
        
            print ("El resultado es: ", resultado)
        
        
    
    else:
        print("Ingresa dato correcto")