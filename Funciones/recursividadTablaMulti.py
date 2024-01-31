def Tabla (n, l=10, m=1):
    if m <= l:
        resultado = n*m
        
        print(f'{n} * {m}: ',resultado)
        
        Tabla(n, l, m+1)
    
        
numero = int (input("Ingrese numero de la tabla: "))


print(Tabla(numero))