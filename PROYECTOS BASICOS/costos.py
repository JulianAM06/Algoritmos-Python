import numpy as np

x = int(input("Ingresa la cantidad de grupos a Costear: "))

PS = 0.4635
CD = 220
totalColaboradores = 0
horasDia = 10
diasHabiles = 22
valoresHoras = []
valoresHoraReal = []
horasLaborales = []


for i in range(1, x + 1):

    sal = int(input("Ingresa Salario: "))
    hor = int(input("Ingresa Horas: "))

    porcentajeSalario = (sal * PS) + sal
    valorHoraInicial = porcentajeSalario / CD

    valoresHoras.append(valorHoraInicial)
    horasLaborales.append(hor)

    total = hor * valorHoraInicial

    totalColaboradores += total 
    
costos = int(input("Ingresa valor de Costos Fijos: "))

colaboradores = int(input("Ingresa cantidad de Colaboradores: "))

CP = colaboradores * horasDia * diasHabiles

totalCostosFijos = costos / CP

for i in valoresHoras:

    z = i + totalCostosFijos

    valoresHoraReal.append(z)

listaHorasReal = np.array(valoresHoraReal)
listaHorasLaborales = np.array(horasLaborales)

resultado = listaHorasReal * listaHorasLaborales

costoTotal = sum(resultado)

por = int(input("Ingresa porcentaje de ganancia: "))

cambio = por / 100

T = (costoTotal * cambio) + costoTotal

utilidad = T - costoTotal

print("El Costo Real es: ",round(costoTotal,2))
print("El Valor Real de la App es: ",round(T,2))
print("La ganancia Real es: ",round(utilidad,2))




