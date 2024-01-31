cantidadCartas = int(input("Ingrese cantidad de Cartas: "))

i = 0
valorTotalTE1 = 0
valorGlobalTE1 = 0
valorTotalTE2 = 0
valorGlobalTE2 = 0
valorTotalTE3 = 0
valorGlobalTE3 = 0
valorTotalTE4 = 0
valorGlobalTE4 = 0
valorTotalTE5 = 0
valorGlobalTE5 = 0
valorTotalTE6 = 0
valorGlobalTE6 = 0



if cantidadCartas > 0:
    
    for i in range (cantidadCartas):
        
        valorGramo = int(input("Ingrese valor del gramo: "))
        pesoCarta = float(input("Ingrese peso de Carta en gramos: "))
        tipoEnvio = int(input("Ingrese\nCorriente--1\nRecomendado--2\nTipo de envio: "))
        lugarEnvio = int (input("Ingrese\nLocal--3\nNacional--4\nInternacional--5\nLugar de envio: "))
        
        if tipoEnvio == 1 and lugarEnvio == 3:
            
            valorTotalPesoCarta = pesoCarta * valorGramo
            valorTotalTE1 = valorTotalPesoCarta + (100 * 0.16) + 100 #Precio Base
            valorGlobalTE1 = valorGlobalTE1 + valorTotalTE1
            
            
            print("Ingreso Total Envios Corriente + Local: ",valorGlobalTE1)
            
        elif tipoEnvio == 1 and lugarEnvio == 4:
            
            valorTotalPesoCarta = pesoCarta * valorGramo
            valorTotalTE2 = valorTotalPesoCarta + (150 * 0.16) + 150 #Precio Base
            valorGlobalTE2 = valorGlobalTE2 + valorTotalTE2
            
            print("Ingreso Total Envios Corriente + Nacional: ",valorGlobalTE2)
            
        elif tipoEnvio == 1 and lugarEnvio == 5:
            
            valorTotalPesoCarta = pesoCarta * valorGramo
            valorTotalTE3 = valorTotalPesoCarta + (200 * 0.16) + 200 #Precio Base
            valorGlobalTE3 = valorGlobalTE3 + valorTotalTE3
            
            print("Ingreso Total Envios Corriente + Internacional: ",valorGlobalTE3)
            
        elif tipoEnvio == 2 and lugarEnvio == 3:
            
            valorTotalPesoCarta = pesoCarta * valorGramo
            valorTotalTE4 = valorTotalPesoCarta + (200 * 0.16) + 200 #Precio Base
            valorGlobalTE4 = valorGlobalTE4 + valorTotalTE4
            
            print("Ingreso Total Envios Recomendado + Local: ",valorGlobalTE4)
            
        elif tipoEnvio == 2 and lugarEnvio == 4:
            
            valorTotalPesoCarta = pesoCarta * valorGramo
            valorTotalTE5 = valorTotalPesoCarta + (300 * 0.16) + 300 #Precio Base
            valorGlobalTE5 = valorGlobalTE5 + valorTotalTE5
            
            print("Ingreso Total Envios Recomendado + Nacional: ",valorGlobalTE5)    
        
        elif tipoEnvio == 2 and lugarEnvio == 5:
            
            valorTotalPesoCarta = pesoCarta * valorGramo
            valorTotalTE6 = valorTotalPesoCarta + (400 * 0.16) + 400 #Precio Base
            valorGlobalTE6 = valorGlobalTE6 + valorTotalTE6
            
            print("Ingreso Total Envios Recomendado + Internacional: ",valorGlobalTE6)
            
            
    print ("Ingreso Total de Envios Corrientes: ", valorGlobalTE1 + valorGlobalTE2 + valorGlobalTE3)    
    print ("Ingreso Total de Envios Recomendados: ", valorGlobalTE4 + valorGlobalTE5 + valorGlobalTE6)    
    print ("Ingreso Total Envios Locales: ",valorGlobalTE1 + valorGlobalTE4)
    print ("Ingreso Total Envios Nacionales: ",valorGlobalTE2 + valorGlobalTE5)
    print ("Ingreso Total Envios Internacionales: ",valorGlobalTE3 + valorGlobalTE6)
    print ("Ingreso Total de Todos los Envios: ", valorGlobalTE1 + valorGlobalTE2 + valorGlobalTE3 + valorGlobalTE4 + valorGlobalTE5 + valorGlobalTE6)
            
        



