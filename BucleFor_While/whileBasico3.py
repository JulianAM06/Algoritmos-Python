numI = int(input("Ingrese numero inicial: "))
numF = int (input("Ingrese nuemro final: "))
cantidad = 0

while numI < numF:
    if numI % 2 ==0:
        print(numI)
        cantidad +=1
    numI +=1
    
print ("hay", cantidad, "numeros pares")
    