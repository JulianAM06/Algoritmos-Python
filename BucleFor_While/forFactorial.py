x = int(input("Ingresar numero para limite del factorial: "))

F = 1

for i in range(1, x + 1):

    F = F * i

print("El factorial es: ",F)

