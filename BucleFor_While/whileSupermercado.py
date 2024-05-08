i = True

P = 0 #Acomulador

j = 0 #Contador

while i == True:

    x = int(input("Ingresa valor del producto: ")) 

    if x != 0:

        P += x

        j += 1

    else:

        i = False

print(P)
print(j)