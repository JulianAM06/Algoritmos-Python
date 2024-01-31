def Calcular_Vocal(string):
    
    lista = ['a', 'e', 'i', 'o', 'u']
    
    if string in lista:
        return True
    else:
        return False


string = str(input("Ingrese letra: "))

C = Calcular_Vocal(string)

print(C)