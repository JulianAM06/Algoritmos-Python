
radio = float(input("Ingrese radio: "))
altura = float(input("Ingrese altura: "))

def area(radio):
    
    PI = 3.1416
    
    return PI * (radio**2)

def volumen(altura):
   return area(radio) * altura
    
print(area(radio))
print(volumen(altura))