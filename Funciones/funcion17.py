def Calcular_Max(n1, n2, n3):
    
    if n1 > n2 and n1 > n3:
        return n1
    
    elif n2 > n1 and n2 > n3:
        return n2
    
    else:
       return n3

n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
n3 = int(input("Ingrese tercer numero: "))

C = Calcular_Max(n1, n2, n3)

print(C)