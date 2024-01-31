comprobar = True

while comprobar == True:
    
    n = (input("Ingresa numero entre el 0 y 999: "))
    
    if n > "0":
        comprobar = False
        
        print(len(n))
        
    else:
        print("Ingresa dato correcto... Intenta nuevamente")
        