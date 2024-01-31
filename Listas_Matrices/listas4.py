numeros = [1,2,9,7,8,5,6]

n = int(input("Ingrese el numero a buscar: "))

i=0
p = 0

while i in numeros:
    
    if numeros[i]==n:
        p = i
        
        i = i+1
        
print(p)