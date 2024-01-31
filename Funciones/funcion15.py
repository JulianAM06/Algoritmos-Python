def CalcularSegundos(D,H,M,S):
    
    CSD = D * 86400
    CSH = H * 3600
    CSM = M * 60
    CSS = S * 1
    
    TS = CSD + CSH + CSM + CSS
    
    return TS



D = int(input("Ingrese cantidad de Dias: "))
H = int(input("Ingrese cantidad de Horas: "))
M = int(input("Ingrese cantidad de minutos: "))
S = int(input("Ingrese cantidad de segundos: "))

TS = CalcularSegundos(D, H, M, S)

print("La cantidad de segundos es: ",TS)