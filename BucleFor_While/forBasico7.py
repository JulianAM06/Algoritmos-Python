CA = int(input("Ingrese cantidad de autos vendidos: "))

i = 0
CVA = 0
CVB = 0
CVC = 0

if CA > 0:
    
    for i in range (CA):
        
        TA = int(input("Ingrese\n1--Carro A\n2--Carro B\n3--Carro C\nPara saber el tipo de Carro: "))
        
        
        if TA == 1:
            
            CVA = CVA + 24
            
        elif TA == 2:
            
            CVB = CVB + 33
            
        elif TA == 3:
            
            CVC = CVC + 38
            
    CTV = CVA + CVB + CVC
            
    print ("La Comision Total del Vendedor es: ", CTV)