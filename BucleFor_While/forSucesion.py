z = int(input("Ingresa un numero para saber cuantas veces se realizara la operacion: "))
x = int(input("Ingresa un numero para reemplazar en X: "))

e = 0 #Contador

R = 0 #Acumulador

for i in range (1, z + 1, 1): 

    e = e + 2

    formula = (x**e) / i

    R += formula
    
print(R)