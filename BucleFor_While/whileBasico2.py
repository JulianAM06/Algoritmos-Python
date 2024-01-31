numM = int(input("Ingrese el numero a multiplicar: "))
cVeces = int(input("Ingrese cantidad de veces a multiplicar: "))

inicio = 1

while inicio <= cVeces:
    resultado = numM * inicio
    print (numM,'*',inicio, '=',resultado)
    inicio = inicio + 1
    
