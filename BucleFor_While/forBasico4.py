CE = int(input("Ingrese cantidad de Estudiantes a evaluar: "))

if CE > 0:
    
    for i in range(CE):
        
        n1 = float(input("Ingrese nota uno: "))
        n2 = float(input("ingrese nota dos: "))
        n3 = float(input("Ingrese nota tres: "))
        
        PTN = (n1*0.3) + (n2*0.3) + (n3*0.4)
        
        print("Nota final es: ", PTN)
        
        if PTN > 3:
            
            print("El estudiante Gana Curso")
            
        else:
            
            print("El estudiante Pierde Curso")