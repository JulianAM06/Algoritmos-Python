n = int (input("Ingrese la cantidad de autos a revisar: "))

i = 0
cAmarillo = 0
cRosa = 0
cRoja = 0
cVerde = 0
cAzul = 0

if n > 0:
    
    for i in range(n):
        
        UNP = int (input("Ingrese\n1 o 2--Amarillo\n3 o 4--Rosa\n5 o 6--Roja\n7 o 8--Verde\n9 o 0--Azul\nDigito del color: "))
        
        
        if UNP == 1 or UNP ==2:
            cAmarillo = cAmarillo + 1
            
        if UNP == 3 or UNP ==4:
            cRosa = cRosa + 1
            
        if UNP == 5 or UNP ==6:
            cRoja = cRoja + 1
            
        if UNP == 7 or UNP ==8:
            cVerde = cVerde + 1
            
        if UNP == 9 or UNP ==0:
            cAzul = cAzul + 1
            
    print("Cantidad de Calcomanias Amarillas: ",cAmarillo)
    print("Cantidad de Calcomanias Rosa: ",cRosa)
    print("Cantidad de Calcomanias Rojas: ",cRoja)
    print("Cantidad de Calcomanias Verdes: ",cVerde)
    print("Cantidad de Calcomanias Azules: ",cAzul)