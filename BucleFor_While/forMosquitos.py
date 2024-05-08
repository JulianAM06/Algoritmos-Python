x = int(input("Ingresa cantidad de semanas para calcular mosquitos: "))

i = 0

z = 2

R = 0 #Acumulador

for i in range (0, x , 1): 

    y = z**i

    R += y


print(R)






