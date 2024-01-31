#Ingresar el nombre de un empleado, las horas trabajadas, luego Calcular pago bruto, Seguridad Social y total del pago, presentar los resultados del programa. Nota: El seguro social es 84 si el sueldo es mayor 2400, sino es el 3.5% del sueldo del empleado. (50 dolares la hora)


nombre = str(input("Ingresa tu nombre: "))
horasLaborales = int (input("Ingresa horas laborales: "))
valorHoraLaboral = 50

salario = horasLaborales * valorHoraLaboral

if salario > 2400:
    
    totalPagoBruto = salario + 84
    

elif salario < 2400:
    
    totalPagoBruto = (salario * 0.035) + salario
    
    
print(f"El Pago Bruto de {nombre} es:{totalPagoBruto}")    



































"""NB = (input("Ingrese nombre"))
HL = float (input("Ingrese horas laborales"))

VHL = HL*50

if VHL > 2400:
    PB = VHL+84

else: PB = (VHL*0.035)+VHL
    

print("El pago bruto es: ",PB)"""
