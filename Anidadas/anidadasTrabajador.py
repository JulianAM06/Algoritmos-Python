#Ver en el Taller

salario = int(input("Ingrese Salario Trabajador: "))
antiguedadTrabajador = int(input("Ingrese antiguedad del Trabajador en Meses: "))

if antiguedadTrabajador < 12:
    
    utilidad = salario * 0.05
    
elif antiguedadTrabajador >= 12 and antiguedadTrabajador < 24:
    
    utilidad = salario * 0.07
    
elif antiguedadTrabajador >= 24 and antiguedadTrabajador < 60:
    
    utilidad = salario * 0.10
    
elif antiguedadTrabajador >= 60 and antiguedadTrabajador < 120:
    
    utilidad = salario * 0.15
    
else:
    
    utilidad = salario * 0.20
    
    
print("La utilidad del Trabajador es: ", utilidad)
    
    
    
    
    






































"""TL = float (input("Ingrese tiempo labaral en meses "))
SM = float (input("Ingrese salario mensual "))

if TL < 12:
    UL = SM * 0.05

elif TL >= 12 and TL < 24:
    UL = SM * 0.07

elif TL >= 24 and TL < 60:
    UL = SM * 0.10

elif TL >= 60 and TL < 120:
    UL = SM * 0.15

else:
    UL = SM * 0.20

print ("La utilidad anual del trabajador es: ",UL)"""