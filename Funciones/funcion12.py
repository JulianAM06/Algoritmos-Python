def validarPrimo(n):
    
    if n <= 1:
        return False
    
    elif n ==2:
        return True
    
    for i in range(2,n):
        
        if n % i == 0:
            return False
    
    return True


n = int(input("Ingrese numero para validar si es primo: "))

NP = validarPrimo(n)

if NP == True:
    print("El numero es Primo")
    
else:
    print("EL numero no es Primo")