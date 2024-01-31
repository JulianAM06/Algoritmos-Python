VI = float (input("Ingrese valor de la inversion "))
VH = float (input("Ingrese el valor de la hipoteca "))


if VH < 100000000:
   I = VI / 2

else: VH >= 100000000
I = (VI - VH) /2


print ("El valor de la inversion es: ",I)