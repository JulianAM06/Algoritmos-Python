def determinarEC(letra):
    estadosCiviles = {
        'C': 'Casado',
        'S': 'Soltero',
        'D': 'Divorciado',
        'V': 'Viudo',
    }
    estadoCivil = estadosCiviles.get(letra, -1)
    return estadoCivil


numEstado = input("Ingrese la letra correspondiente: \nCasado--C\nSoltero--S\nDivorciado--D\nViudo--V\nPara determinar su estado civil: ").upper()

estadoCivil = determinarEC (numEstado)

if estadoCivil != -1:
    print(f"El estado civil es: {estadoCivil}")

else: 
    print("La letra ingresada es desconocida para el programa")