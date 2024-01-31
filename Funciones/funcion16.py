def CalcularIMC(P, A):
    
    IMC = P / (A * 2)
    
    return IMC


P = float(input("Ingrese el peso en KG: "))
A = float(input("Ingrese la estatura en Metros: "))

IMC = CalcularIMC(P, A)

if IMC < 18.5:
    print("Bajo de Peso")
    
elif IMC >= 18.5 and IMC <= 24.9:
    print("Normal")
    
elif IMC >= 25 and IMC <= 29.9:
    print("Sobrepeso")
    
elif IMC >= 30 and IMC <= 34.9:
    print("Obesidad I")
    
elif IMC >= 35 and IMC <= 39.9:
    print("Obesidad II")
    
elif IMC >= 40 and IMC <= 49.9:
    print("Obesidad III")
    
elif IMC >= 50:
    print("Obesidad IV")
    
    