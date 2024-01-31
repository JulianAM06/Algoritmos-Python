#Una persona es alta cuando es hombre y mide más de 180 CMS o mujer cuando mide más de 175cms. Haga un algoritmo que lea el sexo y la estatura en CMS de una persona e imprima es “ALTA” o “NO ALTA”.

def DeterminarSexo (letra):
    
    sexos = {
        
        'M': 'Masculino',
        'F': 'Femenino'
         
    }
    
    sexo = sexos.get(letra, 0)
    return sexo



letraSexo = input("Ingrese\nHombre--M\nMujer--F\nPara conocer el sexo: ").upper()
altura = int(input("Ingrese la Altura en Centimetros: "))


sexo = DeterminarSexo(letraSexo)

# Condicional para conocer el sexo


if sexo != 0:
    print(f"El sexo de la persona es: {sexo}")
    
else:
    print("La letra ingresada no existe en el programa")


# Condicional para saber si es Alta


if sexo == 'Masculino' and altura > 180:
    
    print("Persona Masculina de ALtura Alta")

elif sexo == 'Femenino' and altura > 175:
    
    print("Persona Femenina de Altura Alta")

else:
    print(f"La persona {sexo} no es Alta")
    





























"""def DeterminarSexo (letra):
    
    sexos = {
        
        'M': 'Hombre',
        'F': 'Mujer'
    }
    
    sexo = sexos.get(letra, 0)
    return sexo


letraSexo = input("Ingrese\nHombre--M\nMujer--F\nPara conocer el Sexo: ").upper()
Altura = int(input("Ingrese altura en Centimetros: "))

sexo = DeterminarSexo(letraSexo)

if sexo != 0:
    
    print(f"El Sexo de la Persona es: {sexo}")
    
else:
    
    print("La letra ingresado es desconocida para el Programa")
    
    
if Altura >= 180 and sexo == 'Hombre':
    
    print("Hombre de Estatura Alta")

    
elif Altura >= 175 and sexo == 'Mujer':
    
    print("Mujer de Estatura Alta")
    
else:
    
    print(f"{sexo} de Estatura No Alta")"""
    
    


