def TablaMultiplicar(n1, n2):
    return str(n1) + '*' + str(n2) + '=' + str(n1*n2)


n = int(input("Ingrese numero entero positivo diferente de cero: "))
x = int (input("Ingrese cantidad de veces a multiplicar: "))

if n > 0:
    
    for i in range(0,x+1):
        
        print(TablaMultiplicar(n,i))