def factorial(n):
    if n==0:
        resultado = 1
        print("Finaliza")
                
    else: 
       resultado = n * factorial(n-1)
       
    
    return resultado
   
n = int(input("ingrese numero: "))

print(factorial(n))
        