CC = int (input("Ingrese la cantidad de Clientes: "))

i = 0
VTP = 0
VTD = 0

if CC > 0:
    
    for i in range (CC):
        
        NC = input("Ingrese nombre del Cliente: ")
        KG = float(input("Ingrese cantidad de kilos a comprar: "))
        VP = float(input("Ingrese valor a pagar: "))
    
        if KG > 10:
            VTP =(VP - (VP * 0.15)) 
            print("Valor total con Descuento: ",VTP)
            
            
            VTD = VTD + VTP
        
            print(VTD)