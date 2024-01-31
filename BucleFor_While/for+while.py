comprobar = True

while comprobar == True:


    num = int (input("Ingrese numero entero positivo para ver su tabla de multiplicacion: "))
    limite = int(input("Ingrese la cantidad de veces a multiplicar: "))

    if num > 0:
        comprobar = False
        for i in range(limite +1):
            resultado = num * i
            print (num,"*",i,"=",resultado)
        
    else:
        print("Ingresa dato correcto")
