x = int (input("Ingrese numero a multiplicar: "))
n = int (input("Ingrese cantida de veces a multiplicar: "))

for i in range (0, n+1):
    
    TM = x * i
    
    print(f"{x} x {i} = {TM}")
    
