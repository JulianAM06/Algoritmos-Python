cantidadNotas = int(input("Ingrese cantidad de Notas a Evaluar: "))

i = 0
notaAprobados = 0
notaDesaprobados = 0


if cantidadNotas > 0:
    
    
    for i in range (cantidadNotas):
        
        Nota = float(input("Ingrese la nota del Estudiante: "))
        
        
        if Nota >= 70:
            
            notaAprobados = notaAprobados + 1
            
        elif Nota < 70:
            
            notaDesaprobados = notaDesaprobados + 1
            
            
    totalNotas = notaAprobados + notaDesaprobados
    
    porcentajeAprobados = (notaAprobados/totalNotas)*100
    
    porcentajeDesaprobados = (notaDesaprobados/totalNotas)*100
    
    print("La cantidad de Notas Aprobadas es: ", notaAprobados)
    print("La cantidad de Notas Desaprobadas es: ", notaDesaprobados)
    print("El porcentaje de Notas Aprobadas es: ", porcentajeAprobados)
    print("El porcentaje de Notas Desaprobadas es: ", porcentajeDesaprobados)



























"""CN = int (input("Ingrese cantidad de notas a evaluar: "))


i = 0
NA = 0
ND = 0

if CN > 0:
    
    for i in range (CN):
        
        N = float(input("Ingrese la nota del estudiante: "))
        
        
        if N >= 70:
            NA = NA + 1
            
        if N < 70:
            ND = ND + 1
            
    TN = NA + ND
    PNA = (NA/TN)*100
    PND = (ND/TN)*100
    
    print("Cantidad de Notas Aprobados: ",NA)
    print("Cantidad de Notas Desaprobados: ",ND)
    print("Porcentaje de Aprobados: ",PNA)
    print("Porcentaje de Desaprobados: ",PND)"""