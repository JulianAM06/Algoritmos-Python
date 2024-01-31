cantidadPersonas = int(input("Ingrese cantidad de Personas a Evaluar: "))

i = 0
pesoTotalNiños = 0
pesoTotalJovenes = 0
pesoTotalAdultos = 0
pesoTotalViejos = 0
porcentajePesoNiños = 0
porcentajePesoJovenes = 0
porcentajePesoAdultos = 0
porcentajePesoViejos = 0


if cantidadPersonas >0:
    
    for i in range(cantidadPersonas):
        
        edad = int(input("Ingrese\n(0-12)--Niño\n(13-29)--Jovenes\n(30-59)--Adulto\n(60+)--Viejo\nEdad: "))
        peso = float(input("Ingrese peso de la persona: "))
        
        
        if edad >= 0 and edad <= 12:
            
            pesoTotalNiños += peso
            
        elif edad >= 13 and edad <= 29:
            
            pesoTotalJovenes += peso
            
        elif edad >= 30 and edad <= 59:
            
            pesoTotalAdultos += peso
            
        elif edad >=60:
            
            pesoTotalViejos += peso
            
    pesoTotalPoblacion = pesoTotalNiños + pesoTotalJovenes + pesoTotalAdultos + pesoTotalViejos
        
    
    porcentajePesoNiños = (pesoTotalNiños/pesoTotalPoblacion)*100
    porcentajePesoJovenes = (pesoTotalJovenes/pesoTotalPoblacion)*100
    porcentajePesoAdultos = (pesoTotalAdultos/pesoTotalPoblacion)*100
    porcentajePesoViejos = (pesoTotalViejos/pesoTotalPoblacion)*100
    
    
    print("Peso Total Niños: ",pesoTotalNiños)
    print("Peso Total Jovenes: ",pesoTotalJovenes)
    print("Peso Total Adultos: ",pesoTotalAdultos)
    print("Peso Total Viejos: ",pesoTotalViejos)
    print("Peso Total Poblacion: ",pesoTotalPoblacion)
    print("Promedio peso Niños: ",porcentajePesoNiños)
    print("Promedio peso Jovenes: ",porcentajePesoJovenes)
    print("Promedio peso Adultos: ",porcentajePesoAdultos)
    print("Promedio peso Viejos: ",porcentajePesoViejos)








"""CP = int (input("Ingrese cantidad de personas a evaluar: "))

i = 0
PTN = 0
PTJ = 0
PTA = 0
PTV = 0
PPN = 0
PPJ = 0
PPA = 0
PPV = 0

if CP > 0:
    
    for i in range (CP):
        
        Edad = int(input("Ingrese\n(0-12)--Niño \n(13-29)--Jovenes \n(30-59)--Adulto\n(60+)--Viejo\nEdad: "))
        Peso = float(input("Ingrese peso de la persona: "))
        
        if Edad >=0 and Edad <=12:
            PTN = PTN + Peso
            
        elif Edad >=13 and Edad <=29:
            PTJ = PTJ + Peso
            
        elif Edad >=30 and Edad <=59:
            PTA = PTA + Peso
            
        elif Edad >= 60:
            PTV = PTV + Peso
            
        
        PTP = PTN + PTJ + PTA + PTV
        
        PPN = (PTN/PTP)*100
        PPJ = (PTJ/PTP)*100
        PPA = (PTA/PTP)*100
        PPV = (PTV/PTP)*100
        
        
    print("Peso Total Niños: ",PTN)
    print("Peso Total Jovenes: ",PTJ)
    print("Peso Total Adultos: ",PTA)
    print("Peso Total Viejos: ",PTV)
    print("Peso Total Poblacion: ",PTP)
    print("Promedio peso Niños: ",PPN)
    print("Promedio peso Jovenes: ",PPJ)
    print("Promedio peso Adultos: ",PPA)
    print("Promedio peso Viejos: ",PPV)"""
    
    
       
            
        
            
        
        