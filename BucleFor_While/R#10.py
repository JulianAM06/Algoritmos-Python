n = int (input("Ingrese cantidad de trabajadores: "))

i = 0

if n >0:
    
    for i in range (n):
        
        name = input("Ingrese nombre del trabajador: ")
        HL = float(input("Ingrese cantidad de horas laborales: "))
        SH = float(input("Ingrese valor de la hora salario: "))
        
        if HL <= 40:
            ST = HL * SH
            
            print("Nombre trabajador: ", name)
            print("Salario total: ",ST)
            
        if HL > 40:
            SE = (HL - 40) * (SH * 1.5)
            SN = SH * 40
            ST = SE + SN
            
            print("Nombre trabajador: ", name)
            print("Salario total: ",ST)
            
        