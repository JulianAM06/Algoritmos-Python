def CalcularNota (n1, n2, n3):
    return (n1*0.3) + (n2*0.3) + (n3*0.4)


CE = int(input("Ingrese cantidad de estudiantes a evaluar: "))



for i in range(CE):
    
    n1 = float(input("Ingrese nota uno: "))
    n2 = float(input("ingrese nota dos: "))
    n3 = float(input("Ingrese nota tres: "))
    
    NF = CalcularNota (n1, n2, n3)
    
    print("La nota final es: ", round(NF,2))
    
    if NF > 3:

        print("El estudiante Gana Curso")
        
    else:
        
        print("El estudiante Pierde Curso")
    