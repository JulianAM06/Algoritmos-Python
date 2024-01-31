def Suma (x,n):
    sumar = x + n
    print (f'{x} + {n} es: ',sumar)
    
    return sumar
    

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))


print (Suma(num1,num2))