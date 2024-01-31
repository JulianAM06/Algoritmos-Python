#Ver en el Taller
def determinarEnfermedad (numero):
    
    enfermedades = {
        
        1: 'Cancer',
        2: 'Diabetes',
        3: 'Diarrea',
        4: 'Vomito'
        
    }
    
    enfermedad = enfermedades.get(numero, 0)
    return enfermedad



detEnfermedad = int(input("Ingrese\nCancer--1\nDiabetes--2\nDiarrea--3\nVomito--4\nPara conocer la enfermedad del Paciente: "))
diasHospital = int(input("Ingrese la cantidad de Dias internado en el hospital: "))
edadPaciente = int(input("Si el paciente se encuentra entre 14 y 22 años, Ingrese 1, sino Ingrese 0: "))



enfermedad = determinarEnfermedad(detEnfermedad)



if enfermedad != 0:
    
    print("La enfermedad es: ", enfermedad)
    
else:
    
    print("El numero ingresado no lo reconoce el sistema")
    
    
if enfermedad == 'Cancer'  and edadPaciente == 0:
    
    valorPagoTotal = diasHospital * 25
    
    
elif enfermedad == 'Cancer' and edadPaciente == 1:
    
    valorPago = diasHospital * 25
    
    valorAdicional = valorPago * 0.10
    
    valorPagoTotal = valorPago + valorAdicional
    
    
elif enfermedad == 'Diabetes'  and edadPaciente == 0:
    
    valorPagoTotal = diasHospital * 16
    
    
elif enfermedad == 'Diabetes' and edadPaciente == 1:
    
    valorPago = diasHospital * 16
    
    valorAdicional = valorPago * 0.10
    
    valorPagoTotal = valorPago + valorAdicional
    
    
elif enfermedad == 'Diarrea' and edadPaciente == 0:
    
    valorPagoTotal = diasHospital * 20
    
    
elif enfermedad == 'Diarrea'  and edadPaciente == 1:
    
    valorPago = diasHospital * 20
    
    valorAdicional = valorPago * 0.10
    
    valorPagoTotal = valorPago + valorAdicional
    
elif enfermedad == 'Vomito' and edadPaciente == 0:
    
    valorPagoTotal = diasHospital * 32

elif enfermedad == 'Vomito' and edadPaciente == 1:
    
    valorPago = diasHospital * 32
    
    valorAdicional = valorPago * 0.10
    
    valorPagoTotal = valorPago + valorAdicional
    
else:
    
    print("La enfermedad no existe")
    
print("El valor total a pagar de acuerdo a la edad es: ", valorPagoTotal)
        
    
    
    
    
    
    





































"""def determinarEnfermedad (numero):
    enfermedades = {
        1: 'Enfermedad Cancer',
        2: 'Enfermedad Diabetes',
        3: 'Enfermedad Diarrea',
        4: 'Enfermedad Vomito'
    }
    enfermedad = enfermedades.get(numero, -1)
    return enfermedad



numEnf = int (input("Ingrese numero\nEnfermedad Cancer--1\nEnfermedad Diabetes--2\nEnfermedad Diarrea--3\nEnfermedad Vomito-4\nPara determinar el tipo de Enfermedad: "))
CDH = int (input("Ingrese la cantidad de dias de hospitalizacion: "))
EP = int (input("Si el paciente se encuentra entre 14 y 22 años digite 1, de lo contrario digite 0: "))

enfermedad= determinarEnfermedad(numEnf)


if enfermedad != -1:
    print(f"El numero de enfermedad seleccionada es: {enfermedad}")

else:
    print ("El numero seleccionado es desconocido por el programa")

if numEnf ==1 and EP ==1:
    VH = CDH * 25
    VI = VH * 0.10
    VTH = VI + VH

elif numEnf ==1 and EP ==0:
    VTH = CDH * 25

elif numEnf ==2 and EP == 1:
    VH = CDH * 16
    VI = VH * 0.10
    VTH = VI + VH

elif numEnf ==2 and EP ==0:
    VTH = CDH * 16

elif numEnf ==3 and EP == 1:
    VH = CDH * 20
    VI = VH * 0.10
    VTH = VI + VH

elif numEnf ==3 and EP ==0:
    VTH = CDH * 20

elif numEnf ==4 and EP == 1:
    VH = CDH * 32
    VI = VH * 0.10
    VTH = VI + VH

elif numEnf ==4 and EP ==0:
    VTH = CDH * 32

print ("El valor a pagar de acuerdo a la enfermedad seleccionada, cantidad de dias y rango de edad es: ",VTH)"""