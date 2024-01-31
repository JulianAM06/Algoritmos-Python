def Potencia (x,n):
    if n==0:
        potencia = 1
    
    else:
        p = Potencia(x,n-1)
        potencia=x*p
        print (f'{x} elevado a {n} es',potencia)
        
    return potencia

b = int(input("Digite la base: "))
e = int(input("Digite el exponente: "))


print(Potencia(b, e))