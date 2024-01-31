n = int (input("Ingrese numero mayor: "))
x = int (input("Ingrese numero menor"))


    
if n > x:
    
    
    if n % x == 0:
        print("El divisor es el MCD: ", x)
        
    elif n % x != 0:
        
       for x in range(n):
           D = (n % x) 
           
    if D == 0:
        print(D)
        
    
    
else:
    print("Intenta nuevamente, primer digito mayor que el segundo digito")