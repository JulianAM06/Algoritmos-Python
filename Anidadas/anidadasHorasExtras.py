#Ver en el Taller


horasLaborales = int(input("Ingrese horas Laborales: "))
valorHoraLaboral = int(input("Ingrese valor hora laboral: "))


if horasLaborales < 40:
    
    salario = horasLaborales * valorHoraLaboral
    
elif horasLaborales >= 40 and horasLaborales <= 48:
    
    horasExtras = horasLaborales - 40 
    
    valorHorasExtra = (horasExtras * valorHoraLaboral) * 2
    
    valorHoraNormal = valorHoraLaboral * 40
    
    salario = valorHorasExtra + valorHoraNormal
    
elif horasLaborales > 48:
    
    horasExtraTriple = horasLaborales - 48
    
    valorHoraExtraTriple = (valorHoraLaboral * horasExtraTriple) * 3
    
    valorHoraExtraDoble = (valorHoraLaboral * 8) * 2
    
    valorHoraNormal = valorHoraLaboral * 40
    
    salario = valorHoraExtraTriple + valorHoraExtraDoble + valorHoraNormal
    
print("El Salario del Trabajador es: ", salario)
    
    

 


































"""horasLaborales = int (input("Ingrese las Horas Laborales: "))
valorHoraLaboral = int (input("Ingrese el valor de la hora laboral: "))


if horasLaborales < 40:
    
    salarioCompleto = valorHoraLaboral * horasLaborales


elif horasLaborales >= 40 and horasLaborales < 48:
    
    horasExtras = horasLaborales - 40
    
    totalHorasExtras = (horasExtras * valorHoraLaboral) * 2
    
    totalHorasNormales = valorHoraLaboral * 40 
    
    salarioCompleto = totalHorasExtras +  totalHorasNormales
    

elif horasLaborales >= 48:
    
    horasExtrasTriple = horasLaborales - 48
    
    totalHorasExtrasTriple = (horasExtrasTriple * valorHoraLaboral) * 3
    
    totalHorasExtrasDoble = (valorHoraLaboral * 8) * 2
    
    totalHorasNormales = valorHoraLaboral * 40
    
    salarioCompleto = totalHorasNormales + totalHorasExtrasDoble + totalHorasExtrasTriple
    
print("El Salario Completo del Trabajador es: ", salarioCompleto)"""
    
    

































