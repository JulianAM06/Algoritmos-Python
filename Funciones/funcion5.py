n = int (input("Ingrese numero positivo para conocer su factorial: "))


def factorial (n):
    
    multiplicacion = 1
    
    for i in range(n):
        
        multiplicacion *= i+1
        
    print(multiplicacion)
    
if n <= 0:
    
    print("Ingresa numero positivo")
    
else:
    factorial(n)