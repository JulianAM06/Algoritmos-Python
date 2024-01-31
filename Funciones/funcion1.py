def calcularIMC (peso, altura):
    
    IMC = peso / (altura**2)
    
    return IMC

peso = float(input("Ingrese peso en KG: "))
altura = float (input("Ingrese altura en Metros: "))


print(calcularIMC(peso, altura))