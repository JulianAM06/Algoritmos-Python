#Calcular el total que una persona debe pagar en una llantería, si el precio de cada llanta es de $80.000 si se compran menos de 5 llantas, y de $70.000 si se compran 5 o más.


llantasCompra = int(input("Ingrese cantidad de Llantas: "))

if llantasCompra < 5:
   
   totalPagoLlantas = llantasCompra * 80000
   
else:
   
   totalPagoLlantas = llantasCompra * 70000
   
   
print("El valor a pagar es: ", totalPagoLlantas)






































"""CLL = int (input("Ingrese cantidad de llantas a comprar "))

if CLL < 5:
   VLL= CLL*80000
else: VLL = CLL*70000

print ("El valor de las llantas es: ",VLL)"""