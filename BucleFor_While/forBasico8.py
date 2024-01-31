i = 0
CP = 5
PC = 0
PI = 0
PB = 0

n = input("Ingrese nombre: ")


for i in range(CP):
    
    CL = int(input("Ingrese:\nRespuesta Correcta--1\nRespuesta Incorrecta--2\nRespuesta Blanco--3\nPara conocer el puntaje final: "))
    
    if CL == 1:
        PC = PC + 5
        
    elif CL == 2:
        PI = PI + 2
        
    elif CL == 3:
        PB = PB + 1
        
PTC = PC 
PTI = PI + PB

PTT = PTC - PTI

print(f"El puntaje de {n} es de: {PTT}")