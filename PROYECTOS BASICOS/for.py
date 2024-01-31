buscar = int (input("Ingrese numero a buscar: "))

for numero in range(10):
    print(numero)

    if numero == buscar:
        print("Numero encontrado: ",buscar)
        break