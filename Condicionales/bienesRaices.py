#Una empresa de bienes raíces ofrece casas de interés social, bajo las siguientes condiciones: Si los ingresos del comprador son menores de $800.000, la cuota inicial será del 15 % del costo de la casa y el resto se distribuirá en pagos mensuales, a pagar en diez años. Si los ingresos del comprador son de $800.000 o más la cuota inicial será del 30 % del costo de la casa y el resto se distribuirá en pagos mensuales a pagar en 7 años. La empresa quiere obtener cuánto debe pagar un comprador por concepto de cuota inicial y cuánto por cada pago mesual.


ingresosMensuales = int(input("Ingrese salario Mensual: "))
valorCasa = int (input("Ingrese valor de la Casa: "))


if ingresosMensuales < 800000:
    
    cuotaInicial = valorCasa * 0.15
    
    valorCasaConDescuento = valorCasa - cuotaInicial
    
    cuotasMensuales = valorCasaConDescuento / 120

elif ingresosMensuales >= 800000:
    
    cuotaInicial = valorCasa * 0.30
    
    valorCasaConDescuento = valorCasa - cuotaInicial
    
    cuotasMensuales = valorCasaConDescuento / 84
    
print(f"La cuota Mensual de acuerdo al Salario es: {round(cuotasMensuales,2)}")
    




































"""CC = float (input("Ingrese costo de la casa"))
ING = float (input("Ingrese los Ingresos del Comprador"))

if ING <= 800000:
    CI = CC*0.15
    CM = (CC-CI)/120

else:  CI= CC*0.30
CM = (CC-CI)/84

print ("LA cuota inicial es: ",CI)
print ("LA cuota mensual es: ",CM)"""  