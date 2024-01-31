def CalcularSalario(S,I):
    
    IS = I / 100
    NS = (S*IS) + S
    
    return NS


S = float(input("Ingrese salario actual: "))
I = float(input("Ingrese incremento de salario: "))

CS = CalcularSalario(S,I)

print("El nuevo salrio es: ",CS)