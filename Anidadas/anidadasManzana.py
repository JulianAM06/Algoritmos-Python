KG = float (input("Ingrese cantidad de kilos de manzana a comprar: "))
VKGM = float (input("Ingrese valor del gramo de Manzana: "))

if KG >= 0 and KG <=2:
    VTM = KG * VKGM

elif KG >= 2.01 and KG <=5:
    VM = KG * VKGM
    VD = (KG * VKGM) * 0.10
    VTM = VM - VD

elif KG >= 5.01 and KG <=10:
    VM = KG * VKGM
    VD = (KG * VKGM) * 0.15
    VTM = VM - VD

else: 
    VM = KG * VKGM
    VD = (KG * VKGM) * 0.20
    VTM = VM - VD

print ("El valor a pagar por la cantidad de gramos es: ",VTM)